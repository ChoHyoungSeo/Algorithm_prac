import sys
tot = int(sys.stdin.readline())
num = int(sys.stdin.readline())
ans = 0
for _ in range(num):
  cost, cnt = map(int, sys.stdin.readline().split())
  ans += cost*cnt

print("Yes") if ans == tot else print("No")