from itertools import combinations
n, m = map(int, input().split())
nums = [x+1 for x in range(n)]

ans = list(combinations(nums, m))
for an in ans:
    print(*an)