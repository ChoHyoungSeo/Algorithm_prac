num, tot = map(int, input().split(" "))
coin = []
ans = []

for _ in range(num):
    coin.append(int(input()))
    
for i in range(len(coin)-1, -1, -1):
    if coin[i] <= tot :
        ans.append(tot//coin[i])
        tot = tot % coin[i]
    else:
        continue

print(sum(ans))