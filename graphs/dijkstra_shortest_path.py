import heapq

def dijkstra(graph, source):
    n = len(graph)
    dist = [float('inf')] * n
    dist[source] = 0
    pq = [(0, source)]  # (distance, vertex)

    while pq:
        current_dist, u = heapq.heappop(pq)
        if current_dist > dist[u]:
            continue
        for v, weight in graph[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))
    return dist

# --- User Input ---
n = int(input("Enter the number of vertices: "))
graph = [[] for _ in range(n)]
e = int(input("Enter the number of edges: "))

print("Enter each edge in the format: u v weight")
for _ in range(e):
    u, v, w = map(int, input("Edge: ").split())
    graph[u].append((v, w))
    graph[v].append((u, w))  # For undirected graph

src = int(input("Enter the source vertex: "))
result = dijkstra(graph, src)

# --- Output ---
print("Shortest distances from source:", result)
