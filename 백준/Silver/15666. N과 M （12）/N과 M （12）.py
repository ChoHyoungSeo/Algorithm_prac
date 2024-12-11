from itertools import combinations_with_replacement

_, target = map(int, input().split())
nums = sorted(set(map(int, input().split())))

result = combinations_with_replacement(nums, target)

for num in result:
    print(*num)