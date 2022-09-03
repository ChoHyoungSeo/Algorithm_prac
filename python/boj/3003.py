import sys
my_chess = list(map(int, sys.stdin.readline().split()))
std = [1,1,2,2,2,8]
ans = []

for std_idx, my_chess_idx in zip(std, my_chess):
  ans.append(std_idx - my_chess_idx)

print(*ans)