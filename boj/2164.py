#using list - timeover error

# a = int(input())
# k = []

# for i in range(a):
#     k.append(i+1)

# for i in range(a-1):
#     k = k[1:]
#     k.append(k[0])
#     k = k[1:]
# print(k[0])

# new_answer using deque

from collections import deque

a = int(input())
queue = deque()

for i in range(a):
    queue.append(i + 1) 

while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())
print(queue.pop())