tot = int(input())
cnt, tick = 1, 0
stack = []
ans = []

for _ in range(tot):
    n = int(input())
    while cnt <= n:
        stack.append(cnt)
        cnt += 1
        ans.append("+")
    if stack[-1] == n:
        ans.append("-")
        stack.pop()
    else:
        print("NO")
        tick = 1
        break
if not tick:
    for a in ans:
        print(a, end="\n")