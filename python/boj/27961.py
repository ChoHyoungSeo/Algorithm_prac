target=int(input())
ans = 0
cats = 0
while target > cats:
    if cats == 0:
        cats += 1
        ans += 1
    else:
        cats *= 2
        ans += 1

print(ans)