num, std = map(int, input().split())
numList = list(map(int, input().split()))
ans = []

for i in range(num):
    if numList[i] < std:
        ans.append(numList[i])
    else:
        continue
        
for i in range(len(ans)):
    print(ans[i], end = " ")