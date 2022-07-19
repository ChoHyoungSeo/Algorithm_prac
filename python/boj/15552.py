import sys
a = int(sys.stdin.readline().rstrip())

for _ in range(a):
    print(sum(map(int, sys.stdin.readline().split())))