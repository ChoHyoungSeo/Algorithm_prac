tot = int(input())
nums = []
dp = [0] * tot
for i in range(tot):
    tmp = int(input())
    temp = []
    nums.append(tmp)
    dp[i] += tmp
    for j in range(len(nums)):
        if nums[j] < tmp:
            temp.append(dp[j])
    if temp:
        dp[i] += max(temp)
print(max(dp))