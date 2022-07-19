#1874
tot = int(input())
stack = []
ans = []
cnt = 1
tick = 0

for _ in range(tot):
    tmp = int(input())

    while cnt <= tmp:
        stack.append(cnt)
        cnt += 1
        ans.append("+")

    if stack[-1] == tmp:
        ans.append("-")
        stack.pop()
    
    else:
        print("NO")
        tick = 1
        break
        
if not tick:
    for a in ans:
        print(a)