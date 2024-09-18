import sys
input = sys.stdin.readline

stack = []
n = int(input())

for _ in range(n):
  comm = input().strip()
  if comm == "top":
    print(stack[-1] if stack else -1)
  elif comm == "empty":
    print(0 if stack else 1)
  elif comm == "size":
    print(len(stack))
  elif comm == "pop":
    print(stack.pop() if stack else -1)
  else:
    com, num = comm.split()
    stack.append(int(num))
