import sys

N = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))
maxDP = arr[:]
minDP = arr[:]

for _ in range(N - 1):
    a, b, c = map(int, sys.stdin.readline().split())
    maxDP = [
        a + max(maxDP[0], maxDP[1]), 
        b + max(maxDP), 
        c + max(maxDP[1], maxDP[2])
    ]
    minDP = [
        a + min(minDP[0], minDP[1]), 
        b + min(minDP), 
        c + min(minDP[1], minDP[2])
    ]

print(max(maxDP), min(minDP))
