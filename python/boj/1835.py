from collections import deque
n = int(input())
queue = deque()
queue.append(n)

for i in range(n-1, 0, -1):
    queue.appendleft(i)
    for j in range(i):
        queue.appendleft(queue.pop())

print(*queue)