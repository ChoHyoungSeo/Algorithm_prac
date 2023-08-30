import heapq
import sys
input = sys.stdin.readline
heap = []

tot = int(input())
for _ in range(tot):
    n = int(input())
    if n == 0:
        if not heap:
            print(0)
        else:
            print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap, -n)