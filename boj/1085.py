ans = []
x,y,w,h = map(int, input().split())
ans.append(x)
ans.append(y)
ans.append(w-x)
ans.append(h-y)

ans.sort()

print(ans[0])