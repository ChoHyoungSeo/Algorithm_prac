import sys

a = int(sys.stdin.readline().rstrip())
ans = 0

for i in range(1, a):
    numList = list(map(int, str(i)))
    if i + sum(numList) == a:
        ans = i
        break
    else:
        continue
print(ans)