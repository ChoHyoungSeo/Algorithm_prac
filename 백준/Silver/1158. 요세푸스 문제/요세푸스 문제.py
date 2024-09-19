from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().strip().split())
nums = deque([i+1 for i in range(n)])
ans = []

while n != len(ans):
  for _ in range(k-1):
    nums.append(nums.popleft())
  ans.append(nums.popleft())
print("<" + ', '.join(map(str, ans)) + ">")
