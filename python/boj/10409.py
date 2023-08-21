_, t = map(int, input().split())
works = list(map(int, input().split()))
ans = 0

for work in works:
    t -= work
    if t >=0:
        ans += 1
    else:
        break
print(ans)