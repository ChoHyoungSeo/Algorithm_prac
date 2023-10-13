import sys
input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
moves = [tuple(map(int, input().split())) for _ in range(M)]

# 8방향
dy8 = (0, -1, -1, -1, 0, 1, 1, 1)
dx8 = (-1, -1, 0, 1, 1, 1, 0, -1)

# 대각 4방향
dy4 = (-1, -1,  1, 1)
dx4 = (-1,  1, -1, 1)

clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)] # 초기 구름 좌표

def move_clouds(d, s):
    moved_clouds = []
    for y, x in clouds:
        ny = (y + dy8[d-1] * s) % N 
        nx = (x + dx8[d-1] * s) % N
        board[ny][nx] += 1
        moved_clouds.append((ny, nx))
    return moved_clouds

def magic(moved_clouds):
    for y, x in moved_clouds:
        cnt = 0
        for d in range(4):
            ny = y + dy4[d]
            nx = x + dx4[d]
            if 0 <= ny < N and 0 <= nx < N and board[ny][nx] > 0:
                cnt += 1
        board[y][x] += cnt

def make_new_clouds(moved_clouds):
    new_clouds = []
    for y in range(N):
        for x in range(N):
            if (y, x) not in moved_clouds and board[y][x] >= 2:
                board[y][x] -= 2
                new_clouds.append((y, x))
    return new_clouds

for d, s in moves:
    moved_clouds = move_clouds(d, s)
    magic(moved_clouds)
    clouds = make_new_clouds(moved_clouds)

result = sum(sum(row) for row in board)
print(result)
