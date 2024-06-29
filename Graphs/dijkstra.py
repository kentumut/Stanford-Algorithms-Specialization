import sys

# Read the file and parse the graph
def read_graph(file_path):
    graph = {}
    with open(file_path, 'r') as f:
        for line in f:
            parts = line.split()
            node = int(parts[0])
            edges = []
            for edge in parts[1:]:
                target, weight = map(int, edge.split(','))
                edges.append((target, weight))
            graph[node] = edges
    return graph

# Dijkstra's algorithm without using a heap
def dijkstra(graph, start_vertex):
    # Initialize distances and visited set
    num_vertices = len(graph)
    distances = {v: float('inf') for v in graph}
    distances[start_vertex] = 0
    visited = set()
    
    while len(visited) < num_vertices:
        # Select the unvisited vertex with the smallest distance
        min_distance = float('inf')
        min_vertex = None
        for vertex in distances:
            if vertex not in visited and distances[vertex] < min_distance:
                min_distance = distances[vertex]
                min_vertex = vertex
        
        if min_vertex is None:
            break
        
        # Update distances to neighboring vertices
        for neighbor, weight in graph[min_vertex]:
            if neighbor not in visited:
                new_distance = distances[min_vertex] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
        
        # Mark the vertex as visited
        visited.add(min_vertex)
    
    return distances

# Main function to run the algorithm and print the results
def main():
    file_path = 'dijkstra data.txt'
    graph = read_graph(file_path)
    start_vertex = 1
    distances = dijkstra(graph, start_vertex)
    
    # Specified vertices
    specified_vertices = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
    results = []
    for vertex in specified_vertices:
        if distances[vertex] == float('inf'):
            results.append(1000000)
        else:
            results.append(distances[vertex])
    
    # Print results as a comma-separated string
    print(','.join(map(str, results)))

if __name__ == '__main__':
    main()
