#11659
# timeout
# import sys

# tot_nums, tar = map(int, sys.stdin.readline().strip().split())
# nums = list(map(int, sys.stdin.readline().strip().split()))

# for _ in range(tar):
#     start, end = map(int, sys.stdin.readline().strip().split())
#     print(sum(nums[start-1:end]))

#use prefix_sum
import sys
 
tot_nums, tar = map(int, sys.stdin.readline().strip().split())
nums = list(map(int, sys.stdin.readline().strip().split()))
prefix_sum = [0]    # init prefix_sum
temp = 0

for i in nums:    # accumulate arr section 
    temp += i
    prefix_sum.append(temp)
 
for i in range(tar):
    start, end = map(int, sys.stdin.readline().strip().split())
    print(prefix_sum[end] - prefix_sum[start-1])