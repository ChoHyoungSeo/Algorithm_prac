a = int(input())
ans = '%.300f' % (1 / 2**a)
target = 0

for i in range(len(ans)-1, 1, -1):
    if ans[i] != '0':
        target = i
        break
print(ans[:target+1])