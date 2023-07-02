# #using bfs
# #2606 using dfs
# from collections import deque

# tot = int(input())
# l = int(input())
# visited = []
# network_dict = {}

# for i in range(1, tot+1):
#     network_dict[i] = set()

# for i in range(l):
#     a, b = map(int, input().split())
#     network_dict[a].add(b)
#     network_dict[b].add(a)

# def bfs(start, network_dict):

#     # q = deque(start)
#     # q = list(start)
#     #int object not iterable error

#     q = [start]
#     while q:
#         for i in network_dict[q.pop()]:
#             if i not in visited:
#                 visited.append(i)
#                 q.append(i)

# bfs(1, network_dict)
# print(len(visited)-1)

from collections import deque

def bfs(x):
    queue = deque()
    queue.append(x)
    visited = [x]
    cnt = 0
    
    while queue:
        now = queue.popleft()
        cnt += 1
        for k in graph[now]:
            if k not in visited:
                queue.append(k)
                visited.append(k)
    return cnt-1

computers = int(input())
edges = int(input())
graph = [[]* i for i in range(computers+1)]

for _ in range(edges):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
print(bfs(1))