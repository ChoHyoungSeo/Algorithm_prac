from itertools import permutations

n, m = map(int, input().split())
nums = list(map(int, input().split()))

ans = list(permutations(nums, m))
ans.sort()
for num in ans:
  print(*num)