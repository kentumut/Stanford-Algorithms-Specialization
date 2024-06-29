import heapq

def read_graph(filename):
    graph = {}
    with open(filename, 'r') as file:
        for line in file:
            parts = line.split()
            vertex = int(parts[0])
            edges = []
            for edge in parts[1:]:
                neighbor, weight = map(int, edge.split(','))
                edges.append((neighbor, weight))
            graph[vertex] = edges
    return graph

def dijkstra(graph, start_vertex):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start_vertex] = 0
    priority_queue = [(0, start_vertex)]
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_vertex]:
            continue
        
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

def main():
    filename = 'dijkstra_data.txt'  # Change this to the correct file path
    graph = read_graph(filename)
    start_vertex = 1
    distances = dijkstra(graph, start_vertex)
    
    target_vertices = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
    results = []
    for vertex in target_vertices:
        if distances[vertex] == float('infinity'):
            results.append(1000000)
        else:
            results.append(distances[vertex])
    
    result_string = ','.join(map(str, results))
    print(result_string)

if __name__ == "__main__":
    main()
