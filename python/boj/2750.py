a = int(input())
ans = []
for i in range(a):
    ans.append(int(input()))

ans.sort()

for i in range(len(ans)):
    print(ans[i])
