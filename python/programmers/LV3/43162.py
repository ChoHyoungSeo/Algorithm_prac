# dfs
def dfs(computer, computers, visited):
    if visited[computer]:
        return
    visited[computer] = True
    for comp in range(len(computers)):
        if computers[computer][comp] == 1 and not visited[comp]:
            dfs(comp, computers, visited)
    

def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    
    for computer in range(n):
        if not visited[computer]:
            dfs(computer, computers, visited)
            answer += 1
    return answer

# bfs
from collections import deque
def bfs(start, computers, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        computer = queue.popleft()
        for idx, connected in enumerate(computers[computer]):
            if connected == 1 and not visited[idx]:
                queue.append(idx)
                visited[idx] = True
    
def solution(n, computers):
    visited = [False for _ in range(n)]
    answer = 0
    for i in range(n):
        if not visited[i]:
            bfs(i, computers, visited)
            answer += 1
    return answer