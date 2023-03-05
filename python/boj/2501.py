num, std = map(int, input().split())
ans = []

for i in range(1, num+1):
    if num % i == 0:
        ans.append(i)

if len(ans) < std:
    print(0)
else:
    print(ans[std-1])