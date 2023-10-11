# 0 - 빈칸, 1 - 벽, 2 - 바이러스
from collections import deque
import copy
import sys
input = sys.stdin.readline
dir = [(1,0), (0,1), (-1, 0), (0, -1)]
answer = 0

def bfs():
    global answer
    temp_answer = 0
    queue = deque()
    temp_graph = copy.deepcopy(graph)
    #queue에 2의 위치 모두 넣기
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                queue.append((i,j))
    while queue:
        x, y = queue.popleft()
        for dx, dy in dir:
            if x + dx < 0 or y + dy < 0 or x + dx >= n or y + dy >= m: continue
            elif temp_graph[x+dx][y+dy] == 0:
                temp_graph[x+dx][y+dy] = 2
                queue.append((x+dx,y+dy))
            elif temp_graph[x+dx][y+dy] == 1 or temp_graph[x+dx][y+dy] == 2:
                continue
    for i in range(n):
        for j in range(m):
            if temp_graph[i][j] == 0:
                temp_answer += 1
    answer = max(answer, temp_answer)

def make_wall(count):
    if count == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                make_wall(count+1)
                graph[i][j] = 0

if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = [list(map(int,  input().split())) for _ in range(n)]

    make_wall(0)
    print(answer)