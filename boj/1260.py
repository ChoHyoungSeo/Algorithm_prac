#1260
#같은 우선순위의 경우 작은 정점이라는 조건을 생각안해줬구나
#잘 생각해줘야해 set은 순서가 없다.

from collections import deque

def dfs(num_dict, start):
    if start not in visited:
        print(start, end = ' ')
        visited.append(start)
    for i in num_dict[start]:
        if i not in visited:
            print(i, end = ' ')
            visited.append(i)
            dfs(num_dict, i)

def bfs(num_dict, start):
    if start not in visited_bfs:
        tmp.append(start)
        visited_bfs.append(start)
        print(start, end=' ')
    while tmp:
        for i in num_dict[tmp.popleft()]:
            if i not in visited_bfs:
                print(i, end = ' ')
                tmp.append(i)
                visited_bfs.append(i)
                
if __name__ == '__main__':
    tot, edge, start = map(int, input().split())
    num_dict = {}
    tmp = deque()
    visited = []
    visited_bfs = []

    for i in range(tot):
        num_dict[i+1] = set()

    for i in range(edge):
        a,b = map(int, input().split())
        num_dict[a].add(b)
        num_dict[b].add(a)

    for i in range(tot):
        num_dict[i+1] = sorted(deque(num_dict[i+1]))

    dfs(num_dict, start)
    print()
    bfs(num_dict, start)