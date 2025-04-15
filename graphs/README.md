# Graph Algorithms

This folder contains Python implementations of essential graph algorithms, each solving different fundamental problems in graph theory. These are designed to strengthen algorithmic understanding and demonstrate efficient coding practices.

---

## 🔗 Algorithms Included

### 📍 Dijkstra’s Algorithm – Shortest Path
Finds the shortest distance from a source node to all other nodes in a weighted graph using a min-heap (priority queue).

**File:** `dijkstra_shortest_path.py`  
**Concepts:** Greedy algorithm, heap, graph traversal  
**Input:** Number of vertices, number of edges, edges (u, v, weight), source node  
**Output:** List of shortest distances from the source

---

### 🌉 Kruskal’s Algorithm – Minimum Spanning Tree (MST)
Builds an MST by sorting all edges and using Union-Find to avoid cycles.

**File:** `kruskal_minimum_spanning_tree.py`  
**Concepts:** Union-Find (Disjoint Set), greedy edge selection  
**Input:** Number of vertices, number of edges, edges (u, v, weight)  
**Output:** Total cost of MST and list of edges in MST

---

### 🏗️ Prim’s Algorithm – Minimum Spanning Tree (MST)
Constructs the MST starting from any node by always choosing the next minimum-weight edge that connects to the growing MST.

**File:** `prim_minimum_spanning_tree.py`  
**Concepts:** Greedy algorithm, priority queue, visited tracking  
**Input:** Number of vertices, number of edges, edges (u, v, weight)  
**Output:** Total cost of connecting all nodes

---

## 💡 Usage

To run any of the scripts:

```bash
python filename.py
