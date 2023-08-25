h,w = map(int, input().split())
maps = []
real_ans = []
for _ in range(h):
    tmp = list(map(str, input()))
    stack = []
    ans = []
    for i in range(len(tmp)):
        if tmp[i] == 'c':
            stack.append(i)
            ans.append(0)
        elif tmp[i] == '.':
            if not stack:
                ans.append(-1)
            else:
                ans.append(i - stack[-1])
    real_ans.append(ans)
for answer in real_ans:
    print(*answer)