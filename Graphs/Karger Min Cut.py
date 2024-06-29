import random

def merge_and_modify(graph, u, v):
    # Add all edges of v to u, removing self-loops
    graph[u].extend(graph[v])
    graph[u] = [x for x in graph[u] if x != u and x != v]
    
    # Replace all appearances of v with u in the graph
    for vertex in graph:
        graph[vertex] = [u if x == v else x for x in graph[vertex]]
    
    # Remove v from the graph
    del graph[v]

def min_cut(graph):
    while len(graph) > 2:
        # Randomly select an edge
        u = random.choice(list(graph.keys()))
        v = random.choice(graph[u])
        
        # Merge the selected edge's nodes
        merge_and_modify(graph, u, v)
    
    remaining_vertices = list(graph.keys())
    u = remaining_vertices[0]
    v = remaining_vertices[1]
    
    # Count the crossing edges between the remaining two vertices
    cut_edges = sum([1 for x in graph[u] if x == v])
    return cut_edges

# Read graph data from file
file_path = "/Users/kent/Desktop/alles/programmieren/Algorithms Specialization/MinCut.txt"
data_dict = {}
with open(file_path, "r") as f:
    for line in f:
        parts = list(map(int, line.split()))
        key = parts[0]
        value = parts[1:]
        data_dict[key] = value

# Run Karger's Min Cut algorithm multiple times and find the minimum cut
num_trials = 100  # Adjust the number of trials as needed
min_cut_result = float('inf')

for _ in range(num_trials):
    graph_copy = {k: v[:] for k, v in data_dict.items()}
    current_cut = min_cut(graph_copy)
    if current_cut < min_cut_result:
        min_cut_result = current_cut

print("Minimum cut:", min_cut_result)
