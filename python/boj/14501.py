tot = int(input())
pool = [list(map(int, input().split())) for _ in range(tot)]
dp = [0] * tot
for i in range(tot):
    if i + pool[i][0] <= tot: #퇴사 전에 가능한 상담
        dp[i] = pool[i][1] #당일 상담 금액
        for j in range(i):
            if j + pool[j][0] <= i: #이전의 상담들이 오늘 전에 가능한 경우
                dp[i] = max(dp[i], dp[j]+pool[i][1]) # 이전걸 유지 혹은 이전 + 오늘 금액 더한것 최대값.
print(max(dp))