_ = int(input())
nums = list(map(int, input().split()))
ans = sum(nums)
if ans % 3 == 0:
    print('yes')
else:
    print('no')