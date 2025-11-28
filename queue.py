from collections import deque 
q = deque(["steve","el","will"])
q.append("nancy")
q.append("joyce")
print(q)
q.pop()
print(q)
q.popleft()
print(q)
