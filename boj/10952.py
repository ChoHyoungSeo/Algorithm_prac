ans = []
while(True):
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break
    else:
        ans.append(x+y)

for i in range(len(ans)):
    print(ans[i])