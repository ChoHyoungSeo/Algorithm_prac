#나보다 작은게 몇개인가?
#이게 시간초과라...
#index O(N), set O(N), sort O(nlogn)
#18870

# _ = int(input())
# nums = list(map(int, input().split()))
# tmp_nums = list(set(nums))
# ans = []

# tmp_nums.sort()
# for i in range(len(nums)):
#     print(tmp_nums.index(nums[i]), end=' ')
#     # ans.append(tmp_nums.index(nums[i]))

# # print(ans)

import sys

_ = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip().split()))
tmp_nums = sorted(list(set(nums)))

#key point 이런걸 잘 생각해야해
location_dict = {tmp_nums[i]: i for i in range(len(tmp_nums))}

for num in nums:
    print(location_dict[num], end=' ')