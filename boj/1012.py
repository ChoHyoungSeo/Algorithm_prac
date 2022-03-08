#1012
import sys
from collections import deque

def bfs(x, y, graph):
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 0
   
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= row or ny < 0 or ny >= col:
                continue

            elif graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx,ny))

if __name__ == '__main__':
    tot = int(sys.stdin.readline().strip())
   
    for _ in range(tot):
        row, col, veg = map(int, sys.stdin.readline().strip().split())
        graph = [[0]*col for _ in range(row)]
        ans = 0
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
       
        for _ in range(veg):
            tmp_x, tmp_y = map(int, sys.stdin.readline().strip().split())
            graph[tmp_x][tmp_y] = 1
   
        for a in range(row):
            for b in range(col):
                if graph[a][b] == 1:
                    bfs(a,b,graph)
                    ans += 1
        print(ans)