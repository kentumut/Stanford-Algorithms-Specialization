def read_parse_data(filename):
    with open(filename, 'r') as file:
        edges = []
        num_nodes = int(file.readline())  # Read the first line
        for line in file:  # This will automatically start from the second line
            node1, node2, cost = map(int, line.split())
            edges.append((node1, node2, cost))  
    return num_nodes, edges
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, item):
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot == yroot:
            return
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1
def cluster(num_nodes, edges, k):
    uf = UnionFind(num_nodes)
    edges.sort(key=lambda x: x[2])  # Sort edges by cost
    
    num_clusters = num_nodes
    max_spacing = 0

    for edge in edges:
        if num_clusters == k:
            break
        
        node1, node2, cost = edge
        if uf.find(node1 - 1) != uf.find(node2 - 1):  # If nodes are in different clusters
            uf.union(node1 - 1, node2 - 1)  # Merge clusters
            num_clusters -= 1

    # Find the max spacing
    for edge in edges:
        node1, node2, cost = edge
        if uf.find(node1 - 1) != uf.find(node2 - 1):
            max_spacing = cost
            break

    return max_spacing

def main():
    filename = "clustering1.txt"
    num_nodes, edges = read_parse_data(filename)
    
    k = 4  # Number of clusters
    max_spacing = cluster(num_nodes, edges, k)
    print(f"The maximum spacing of a {k}-clustering is: {max_spacing}")

if __name__ == "__main__":
    main()