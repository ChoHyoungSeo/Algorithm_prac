_, std = map(int, input().split())
nums = list(map(int, input().split()))
ans = []
for i in range(0, len(nums)-std+1):
    ans.append(sum(nums[i:i+std]))
print(max(ans))