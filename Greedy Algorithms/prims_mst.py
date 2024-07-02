def read_graph(file_path):
    graph = {}
    with open(file_path, 'r') as f:
        num_nodes, num_edges = map(int, f.readline().split())
        for line in f:
            node1, node2, cost = map(int, line.split())
            if node1 not in graph:
                graph[node1] = []
            if node2 not in graph:
                graph[node2] = []
            graph[node1].append((node2, cost))
            graph[node2].append((node1, cost))
    return graph

def prim_mst(graph):
    start_vertex = next(iter(graph))  # Start from any vertex
    mst_cost = 0
    visited = set([start_vertex])
    num_nodes = len(graph)

    while len(visited) < num_nodes:
        min_cost = float('inf')
        min_edge = None

        for node in visited:
            for neighbor, cost in graph[node]:
                if neighbor not in visited and cost < min_cost:
                    min_cost = cost
                    min_edge = (node, neighbor, cost)

        if min_edge is None:
            break  # Graph is not connected

        _, to_node, edge_cost = min_edge
        visited.add(to_node)
        mst_cost += edge_cost

    return mst_cost

def main():
    file_path = 'edges.txt'
    graph = read_graph(file_path)
    mst_cost = prim_mst(graph)
    print(f"The cost of the minimum spanning tree is: {mst_cost}")

if __name__ == '__main__':
    main()