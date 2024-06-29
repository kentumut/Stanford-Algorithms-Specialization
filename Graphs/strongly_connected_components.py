import os
from collections import defaultdict, deque

class DirectedGraph:
    class Node:
        def __init__(self, key, value):
            self._key = key
            self.value = value
            self.out_neighbors = set()
            self.in_neighbors = set()

        @property
        def key(self):
            return self._key

    def __init__(self, edge_data):
        self.nodes = {}
        self.key_to_index = {}
        self.index_to_key = []
        index = 0
        for first, second in edge_data:
            if first not in self.nodes:
                from_node = self.MakeNode(first, first, index)
                index += 1
            else:
                from_node = self.nodes[first]
            
            if second not in self.nodes:
                to_node = self.MakeNode(second, second, index)
                index += 1
            else:
                to_node = self.nodes[second]
            
            self.AddEdge(from_node, to_node)

    def MakeNode(self, value, key, index):
        node = self.Node(key, value)
        self.nodes[key] = node
        self.key_to_index[key] = index
        self.index_to_key.append(key)
        return node

    def AddEdge(self, from_node, to_node):
        if not from_node or not to_node:
            return
        from_node.out_neighbors.add(to_node)
        to_node.in_neighbors.add(from_node)

    def DFS(self, is_first_pass, node, visited, finishing_order=None, scc=None):
        if not node:
            return
        
        finished = [False] * self.N()
        stack = [node]
        
        while stack:
            node = stack[-1]
            key = self.key_to_index[node.key]

            if not visited[key]:
                visited[key] = True
                if not is_first_pass and scc is not None:
                    scc.append(node.key)

                neighbors = node.in_neighbors if is_first_pass else node.out_neighbors

                for neighbor in neighbors:
                    if not visited[self.key_to_index[neighbor.key]]:
                        stack.append(neighbor)
            else:
                if is_first_pass and finishing_order is not None and not finished[key]:
                    finished[key] = True
                    finishing_order.append(node)
                stack.pop()

    def N(self):
        return len(self.nodes)

    def GetStronglyConnectedComponents(self):
        finishing_order = []
        visited = [False] * self.N()
        
        for node in self.nodes.values():
            if not visited[self.key_to_index[node.key]]:
                self.DFS(True, node, visited, finishing_order)

        sccs = []
        visited = [False] * self.N()
        while finishing_order:
            node = finishing_order.pop()
            scc = []
            if not visited[self.key_to_index[node.key]]:
                self.DFS(False, node, visited, scc=scc)
            if scc:
                sccs.append(scc)

        return sccs

def GetTop5SCCsSizesDescending(edge_data):
    graph = DirectedGraph(edge_data)
    sccs = graph.GetStronglyConnectedComponents()
    scc_sizes = sorted([len(scc) for scc in sccs], reverse=True)

    assert sum(scc_sizes) == graph.N()

    result = [0] * 5
    for i in range(min(5, len(scc_sizes))):
        result[i] = scc_sizes[i]

    return result

def main():
    filepath = "scc_test_1.txt"
    with open(filepath) as file:
        edge_data = []
        line = []
        for i, x in enumerate(map(int, file.read().split())):
            line.append(x)
            if i % 2 == 1:
                edge_data.append((line[0], line[1]))
                line = []

        top5 = GetTop5SCCsSizesDescending(edge_data)
        print(f"Top 5 SCC sizes: {top5}")
        print()

if __name__ == "__main__":
    main()
