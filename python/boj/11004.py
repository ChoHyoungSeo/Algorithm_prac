import sys
a, b = map(int, sys.stdin.readline().rstrip().split(" "))
print(sorted(list(map(int, sys.stdin.readline().rstrip().split(" "))))[b-1])