import sys
input = sys.stdin.readline

n, m = map(int, input().split())
squares = [list(map(int, input().split())) for _ in range(n)]
cum_squares = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        cum_squares[i][j] = cum_squares[i-1][j] + cum_squares[i][j-1] - cum_squares[i-1][j-1] + squares[i-1][j-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(cum_squares[x2][y2] - cum_squares[x2][y1-1] - cum_squares[x1-1][y2] + cum_squares[x1-1][y1-1])
