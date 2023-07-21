_ = int(input())
nums = list(map(int, input().split()))
people = int(input())
std = len(nums) // people
now = 0

for i in range(0, len(nums)//std):
    tmp = nums[now:now+std]
    print(*sorted(tmp), end=' ')
    now += std