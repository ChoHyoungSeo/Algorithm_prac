#using bfs
#2606 using dfs
from collections import deque

tot = int(input())
l = int(input())
visited = []
network_dict = {}

for i in range(1, tot+1):
    network_dict[i] = set()

for i in range(l):
    a, b = map(int, input().split())
    network_dict[a].add(b)
    network_dict[b].add(a)

def bfs(start, network_dict):

    # q = deque(start)
    # q = list(start)
    #int object not iterable error

    q = [start]
    while q:
        for i in network_dict[q.pop()]:
            if i not in visited:
                visited.append(i)
                q.append(i)

bfs(1, network_dict)
print(len(visited)-1)