from typing import List, Set
import itertools

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

def hamming_neighbors(label: str, distance: int) -> Set[str]:
    neighbors = set()
    indices = range(len(label))
    for flip_indices in itertools.combinations(indices, distance):
        neighbor = list(label)
        for idx in flip_indices:
            neighbor[idx] = '1' if neighbor[idx] == '0' else '0'
        neighbors.add(''.join(neighbor))
    return neighbors

def read_data(filename: str) -> List[str]:
    with open(filename, 'r') as f:
        n, bits = map(int, f.readline().split())
        return [f.readline().strip().replace(' ', '') for _ in range(n)]

def solve_clustering(labels: List[str]) -> int:
    n = len(labels)
    label_to_index = {label: i for i, label in enumerate(labels)}
    uf = UnionFind(n)

    for i, label in enumerate(labels):
        for d in [1, 2]:
            for neighbor in hamming_neighbors(label, d):
                if neighbor in label_to_index:
                    uf.union(i, label_to_index[neighbor])

    return len(set(uf.find(i) for i in range(n)))

labels = read_data('clustering_big.txt')
result = solve_clustering(labels)
print(f"The largest k for a k-clustering with spacing at least 3 is: {result}")