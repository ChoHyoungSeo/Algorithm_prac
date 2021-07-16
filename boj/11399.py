a = int(input())
wtime = list(map(int, input().split()))
ans = 0
tot = 0
wtime.sort()

for i in range(a):
    tot += wtime[i]
    ans += tot
print(ans)