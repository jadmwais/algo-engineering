import heapq

def prim(graph, n):
    visited = [False] * n
    min_heap = [(0, 0)]  # (cost, vertex)
    total_cost = 0

    while min_heap:
        cost, u = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        total_cost += cost

        for v, weight in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (weight, v))

    return total_cost

# --- User Input ---
n = int(input("Enter the number of vertices: "))
graph = [[] for _ in range(n)]
e = int(input("Enter the number of edges: "))

print("Enter each edge in the format: u v weight")
for _ in range(e):
    u, v, w = map(int, input("Edge: ").split())
    graph[u].append((v, w))
    graph[u].append((u, w))  # For undirected graph

# --- Output ---
print("Minimum cost to connect all nodes:", prim(graph, n))
