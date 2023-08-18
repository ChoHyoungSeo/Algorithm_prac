words = list(map(str, input()))
score_dict = {"H": 1, "C": 12, "O": 16}
stack = []

for word in words:
    if word == "(":
        stack.append(word)
        
    elif word == ")":
        ans = 0
        while True:
            target = stack.pop()
            if target == "(":
                break
            ans += target
        stack.append(ans)
        
    elif word in score_dict:
        stack.append(score_dict[word])
        
    else:
        stack[-1] *= int(word)
        
print(sum(stack))