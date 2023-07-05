# DP
import sys

N, K = map(int, sys.stdin.readline().split())
distance = [0] * 100001

if N >= K:
    print(N - K)
    sys.exit()

for i in range(N):
    distance[i] = N - i

for i in range(N + 1, K + 1):
    if i % 2 == 0:
        min_val = distance[i // 2] + 1
    else:
        min_val = min(distance[(i + 1) // 2], distance[(i - 1) // 2]) + 2
    
    distance[i] = min(min_val, distance[i - 1] + 1)

print(distance[K])


#BFS
import sys
from collections import deque

def bfs(start):
    queue = deque([start])
    while queue:
        now = queue.popleft()
        if now == k:
            return array[now]
        for coord in (now-1, now+1, 2*now):
            if 0 <= coord < MAX and not array[coord]:
                array[coord] = array[now] + 1
                queue.append(coord)


MAX = 100001
n, k = map(int, sys.stdin.readline().split())
array = [0] * MAX
print(bfs(n))
