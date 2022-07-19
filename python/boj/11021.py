a = int(input())
ans = []
for i in range(a):
    x,y = map(int, input().split())
    ans.append(x+y)

for i in range(len(ans)):
    print("Case #%d: %d" %(i+1, ans[i]))