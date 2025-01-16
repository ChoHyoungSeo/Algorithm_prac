sticks = input()
stack = []
ans = 0

for i in range(len(sticks)):
    if sticks[i] == "(":
        if sticks[i+1] == ")":
            ans += len(stack)
        else:
            stack.append("(")
            ans += 1
    else:
        if sticks[i-1] != "(":
            stack.pop()

print(ans)