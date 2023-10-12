# 0 - 북, 1 - 동, 2 - 남, 3 - 서
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
cnt = 0

def in_range(x, y, m, n):
    return 0 <= x < m and 0 <= y < n

def clean(x, y, dir, m, n):
    global cnt

    # 현재 위치 청소
    if graph[x][y] == 0:
        graph[x][y] = 2
        cnt += 1

    for _ in range(4):
        # 왼쪽 방향으로 회전
        dir = (dir - 1) % 4
        nx, ny = x + dirs[dir][0], y + dirs[dir][1]

        # 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면
        if in_range(nx, ny, m, n) and graph[nx][ny] == 0:
            return clean(nx, ny, dir, m, n)
        
    # 네 방향 모두 청소가 되어있거나 벽인 경우
    # 바라보는 방향을 유지한 채로 한 칸 후진
    nx, ny = x - dirs[dir][0], y - dirs[dir][1]
    if in_range(nx, ny, m, n) and graph[nx][ny] != 1:  # 벽이 아니라면
        return clean(nx, ny, dir, m, n)
    else:
        return cnt

n, m = map(int, input().split())
r, c, dir = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

ans = clean(r, c, dir, n, m)
print(ans)