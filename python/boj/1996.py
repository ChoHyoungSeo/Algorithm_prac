N = int(input())
dx = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
graph = []
ans = []

for _ in range(N):
    graph.append(list(map(str, input())))

for i in range(N):
    tmp = []
    for j in range(N):
        cnt = 0
        for nx, ny in zip(dx, dy):
            if i + nx < 0 or j + ny < 0 or i + nx >= N or j + ny >= N:
                continue
            if graph[i+nx][j+ny] != '.':
                cnt += int(graph[i+nx][j+ny])
        if graph[i][j] != '.':
            cnt = '*'
        if cnt != '*' and cnt >= 10:
            cnt = 'M'
        tmp.append(cnt)
    ans.append(tmp)
for nums in ans:
    print(''.join(map(str, nums)))