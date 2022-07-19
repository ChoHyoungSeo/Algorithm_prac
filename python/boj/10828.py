import sys

def push(num):
    ans.append(num)

def pop():
    if ans:
        print(ans.pop())
    else:
        print(-1)

def size():
    print(len(ans))

def empty():
    if ans:
        print(0)
    else:
        print(1)

def top():
    if ans:
        print(ans[-1])
    else:
        print(-1)

#input()은 timeover
if __name__ == '__main__':
    a = int(sys.stdin.readline().strip())
    ans = []
    for _ in range(a):
        inp = list(map(str, sys.stdin.readline().strip().split()))
        if inp[0] == "push":
            push(inp[1])
        elif inp[0] == "pop":
            pop()
        elif inp[0] == "size":
            size()
        elif inp[0] == "empty":
            empty()
        elif inp[0] == "top":
            top()