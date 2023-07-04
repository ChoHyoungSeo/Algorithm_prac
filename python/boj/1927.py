import heapq
import sys
input = sys.stdin.readline

heap = []
tot = int(input())
for i in range(tot):
    num = int(input())
    if num == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, num)