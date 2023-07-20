from itertools import combinations

_, target = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
ans = combinations(nums,r=target)

for num in ans:
    print(*num)