a = int(input())
cnt = 0
for i in range(a):
    tmp = []
    check = True
    words = list(map(str,input()))

    for j in range(len(words)-1):
        tmp.append(words[j])
        if words[j+1] != words[j] and words[j+1] in tmp:
            check = False
            break
        else:
            continue
    if check:
        cnt += 1
print(cnt)