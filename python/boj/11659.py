#11659
#use prefix_sum

import sys
 
tot_nums, tar = map(int, sys.stdin.readline().strip().split())
nums = list(map(int, sys.stdin.readline().strip().split()))
prefix_sum = [0]
temp = 0

for i in nums:
    temp += i
    prefix_sum.append(temp)
 
for i in range(tar):
    start, end = map(int, sys.stdin.readline().strip().split())
    print(prefix_sum[end] - prefix_sum[start-1])
