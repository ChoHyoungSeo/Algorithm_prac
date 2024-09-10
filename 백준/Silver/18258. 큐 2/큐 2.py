from collections import deque
import sys
input = sys.stdin.readline

n = int(input().strip())
queue = deque()
for _ in range(n):
    command = input().strip()

    if command == "front":
        print(queue[0]) if queue else print(-1)

    elif command == "back":
        print(queue[-1]) if queue else print(-1)

    elif command == "empty":
        print(0) if queue else print(1)
    elif command == "size":
        print(len(queue))
    elif command == "pop":
        print(queue.popleft()) if queue else print(-1)
    else:
        command, num = command.split()
        queue.append(int(num))
