#2606 using dfs
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

def dfs(start, network_dict):
    for i in network_dict[start]:
        if i not in visited:
            visited.append(i)
            dfs(i, network_dict)

dfs(1, network_dict)
print(network_dict)
print(visited)
print(len(visited)-1)
