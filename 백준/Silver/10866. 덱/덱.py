from collections import deque
import sys
input = sys.stdin.readline

tot = int(input().strip())
deq = deque()

for _ in range(tot):
    command = input().strip()
    if command == "back":
        print(deq[-1] if deq else -1)
    elif command == "front":
        print(deq[0] if deq else -1)
    elif command == "empty":
        print(0 if deq else 1)
    elif command == "size":
        print(len(deq))
    elif command == "pop_back":
        print(deq.pop() if deq else -1)
    elif command == "pop_front":
        print(deq.popleft() if deq else -1)
    else:
        comm, num = command.split()
        if comm == "push_back":
            deq.append(num)
        else:
            deq.appendleft(num)

