e,f,c = map(int, input().split())
e += f
ans = 0
while e >= c:
    ans += e//c
    e = e//c + e%c

print(ans)