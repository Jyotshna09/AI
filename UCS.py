import heapq

graph = {
    'A': [('B',1), ('C',4)],
    'B': [('D',2), ('E',5)],
    'C': [('F',1)],
    'D': [('G',3)],
    'E': [('G',1)],
    'F': [],
    'G': []
}

pq = [(0, 'A')]
visited = set()

print("UCS Traversal:")

while pq:
    cost, node = heapq.heappop(pq)

    if node in visited:
        continue

    print(node, "with cost", cost)
    visited.add(node)

    if node == 'G':
        print("Total Cost =", cost)
        break

    for nxt, c in graph[node]:
        heapq.heappush(pq, (cost + c, nxt))
