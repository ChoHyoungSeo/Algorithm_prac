def solution(n):
    dp = [1,1]
    if n < 2:
        return 1
    for i in range(2, n+1):
        dp.append(dp[i-1]*i)
        if dp[i] == n:
            return i
        elif dp[i] > n:
            return i-1