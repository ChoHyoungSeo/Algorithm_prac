#10만, 1초라서 NlogN이하로 떨어뜨리기
import sys
input = sys.stdin.readline
import heapq

heap = []
n = int(input())
for _ in range(n):
    x = int(input())
    if x == 0:
        if heap:
            absolute, original = heapq.heappop(heap) #logN
            print(original)
        else:
            print(0)
    else:
        heapq.heappush(heap, (abs(x), x)) #logN