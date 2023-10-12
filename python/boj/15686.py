# 0 - 빈칸, 1- 집, 2 - 치킨
import sys
input = sys.stdin.readline
from itertools import combinations

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
chikens = []
houses = []
ans = n**3

for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            chikens.append((i,j))
        elif graph[i][j] == 1:
            houses.append((i,j))

for comb in list(combinations(chikens, m)):
    dist = 0
    for x, y in houses:
        tmp = n**3
        for nx, ny in comb:
            tmp = min(tmp, abs(x - nx)+abs(y - ny))
        dist += tmp
    ans = min(ans, dist)
print(ans)