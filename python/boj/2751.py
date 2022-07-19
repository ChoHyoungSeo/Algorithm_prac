import sys
a = int(sys.stdin.readline())
ans = []
for i in range(a):
    ans.append(int(sys.stdin.readline()))
for i in sorted(ans):
    print(i)