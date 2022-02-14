#10867
_ = int(input())
nums = list(map(int, input().split()))
nums = sorted(list(set(nums)))

for i in range(len(nums)):
    print(nums[i], end=' ')