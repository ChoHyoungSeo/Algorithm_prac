#10845
from collections import deque
import sys

def push(x:int):
    ans.append(x)

def pop():
    if ans:
        print(ans.popleft())
    else:
        print(-1)

def size():
    print(len(ans))

def empty():
    if ans:
        print(0)
    else:
        print(1)

def front():
    if not ans:
        print(-1)
    else:
        print(ans[0])

def back():
    if not ans:
        print(-1)
    else:
        print(ans[-1])

if __name__ == '__main__':
    ans = deque()
    n = int(input())
    for i in range(n):
        comm = sys.stdin.readline().strip().split()

        if comm[0] == 'push':
            push(int(comm[1]))
        elif comm[0] == 'pop':
            pop()
        elif comm[0] == 'size':
            size()
        elif comm[0] == 'empty':
            empty()
        elif comm[0] == 'front':
            front()
        else:
            back()