a = int(input())
ans = []
test = []
cnt = 0

for _ in range(a):
    test.append(input())

for i in test:
    for j in range(len(i)):
        if i[j] == "O":
            cnt += 1
            ans.append(cnt)
        else:
            cnt = 0
            ans.append(cnt)
        
        if len(ans) == len(i):
            print(sum(ans))
            cnt = 0
            ans = []