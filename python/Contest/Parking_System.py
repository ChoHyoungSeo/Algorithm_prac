# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

from collections import deque
import sys
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, ans):
	q = deque()
	q.append((x,y))
	while q:
		x, y= q.popleft()
		if graph[x][y] == 0:
			graph[x][y] = 1
			ans += 1
		elif graph[x][y]== 2:
			graph[x][y] = 1
			ans -= 2
		for i in range(4):
			nx = x+dx[i]
			ny = y+dy[i]
			
			if nx < 0 or ny < 0 or nx >= M or ny >= N:
				continue
			if graph[nx][ny] == 0:
				graph[nx][ny] = 1
				q.append((nx, ny))
				ans += 1
			elif graph[nx][ny] == 2:
				graph[nx][ny] = 1
				q.append((nx, ny))
				ans -= 2
			else:
				continue
	return ans
		
M,N = map(int, input().split())
graph = []
ans_candid = []
for _ in range(M):
	graph.append(list(map(int, sys.stdin.readline().strip().split())))
	# graph.append(list(map(int, input().split())))
for i in range(M):
	for j in range(N):
		if graph[i][j] != 1:
			ans = 0
			ans_candid.append(bfs(i, j, ans))
		else:
			continue

if ans_candid and max(ans_candid) > 0:
	print(max(ans_candid))
else:
	print(0)