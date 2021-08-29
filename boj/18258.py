#time complexity should be O(1)
from collections import deque
import sys
dek = deque()
a = int(sys.stdin.readline().strip())
for i in range(a):
    com = list(sys.stdin.readline().strip().split())
    if com[0] == 'push':
        dek.append(com[1])
    elif com[0] == 'pop':
        if dek:
            print(dek.popleft())
        else:
            print(-1)
    elif com[0] == 'size':
            print(len(dek))
    elif com[0] == 'empty':
        if dek:
            print(0)
        else:
            print(1)
    elif com[0] == 'front':
        if dek:
            print(dek[0])
        else:
            print(-1)
    elif com[0] == 'back':
        if dek:
            print(dek[-1])
        else:
            print(-1)