import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
arr = list(map(int, input().split()))
d=deque()
for i in range(n):
    d.append((arr[i], i+1))
result = []

current, index = d.popleft()
result.append(index)
for i in range(n-1):
    if current > 0:
        for j in range(current-1):
            d.append(d.popleft())
    else:
        for j in range(-current):
            d.appendleft(d.pop())
    current, index = d.popleft()
    result.append(index)
for x in result:
    print(x, end=' ')