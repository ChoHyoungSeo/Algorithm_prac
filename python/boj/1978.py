a = int(input())
num = list(map(int, input().split()))
ans = 0
for i in num:
    cnt = 0
    if i == 1:
        continue

    elif i < 4 and i > 1:
        ans += 1
        continue

    else:
        for j in range(2, i, 1):
            if i % j == 0 :
                cnt += 1
            else:
                continue
                
    if cnt == 0:
        ans += 1

print(ans)