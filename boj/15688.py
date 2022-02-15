# #15688
# tot = int(input())
# nums = []

# for _ in range(tot):
#     nums.append(int(input()))

# nums = sorted(list(nums))
# for i in range(len(nums)):
#     print(nums[i])

import sys
tot = int(sys.stdin.readline())
nums = []

for i in range(tot):
    nums.append(int(sys.stdin.readline()))
for i in sorted(nums):
    print(i)