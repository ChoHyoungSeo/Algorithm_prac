import sys
problemSet = int(sys.stdin.readline().strip())
cnt = 0

for _ in range(problemSet):
    tmp = list(map(int, sys.stdin.readline().strip().split()))
    if sum(tmp) >= 2:
        cnt += 1
    else:
        continue
print(cnt)
        