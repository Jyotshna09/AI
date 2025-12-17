from collections import deque

jug1, jug2, target = 4, 3, 2
visited = set()
queue = deque([(0, 0)])

visited.add((0, 0))

print("Water Jug Steps:")
while queue:
    x, y = queue.popleft()
    print((x, y))

    if x == target or y == target:
        print("Target Reached")
        break

    states = [
        (jug1, y),      
        (x, jug2),        
        (0, y),          
        (x, 0),          
        (x - min(x, jug2 - y), y + min(x, jug2 - y)), 
        (x + min(y, jug1 - x), y - min(y, jug1 - x))   
    ]

    for state in states:
        if state not in visited:
            visited.add(state)
            queue.append(state)
