from itertools import permutations

n, m = map(int, input().split())
nums = list(map(int, input().split()))
ans = list(set(permutations(nums, m)))

for num in sorted(ans):
  print(*num)
  