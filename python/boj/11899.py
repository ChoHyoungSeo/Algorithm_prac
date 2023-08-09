target = input()
tmp = []
for t in target:
    if t == '(':
        tmp.append(t)
    else:
        if tmp:
            if tmp[-1] == '(':
                tmp.pop()
            else:
                tmp.append(t)
        else:
            tmp.append(t)
print(len(tmp))
        