inWord = list(map(str,input()))
ans = []
realAns=[]
for i in range(len(inWord)):
    ans.append(ord(inWord[i])-65)

for i in range(len(ans)):
    if ans[i] < 18:
        realAns.append((ans[i]//3) + 2)
    elif ans[i] == 18:
        realAns.append(7)
    elif ans[i] >= 19 and ans[i] <= 21:
        realAns.append(8)
    else:
        realAns.append(9)
        
print(sum(realAns)+len(realAns))