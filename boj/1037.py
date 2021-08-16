_ = int(input())
nums = list(map(int,input().split()))
nums.sort()

if len(nums) % 2 != 0:
    print(nums[len(nums)//2] ** 2)
else:
    print(nums[0] * nums[-1])