nums = list(map(int, input().split()))
nums.sort()
if nums[0]+nums[1] > nums[-1]:
    print(sum(nums))
else:
    print(2*nums[0] + 2*nums[1] - 1)  #c -> a+b-1