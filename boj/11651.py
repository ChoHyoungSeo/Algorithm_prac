import sys
a = int(sys.stdin.readline())
ans = []

for i in range(a):
    ans.append(list(map(int, sys.stdin.readline().split())))

real_ans = sorted(ans, key = lambda x: (x[1], x[0]))
for i in range(a):
    print("%d %d" %(real_ans[i][0], real_ans[i][1]))

# print(sorted(ans, key = lambda x: (x[1], x[0])), end ="\n")