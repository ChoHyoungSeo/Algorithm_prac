#10만, 1초라서 NlogN이하로 떨어뜨리기
import sys
input = sys.stdin.readline
import heapq

heap = []
n = int(input())
for i in range(n):
    x = int(input())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            absolute, original = heapq.heappop(heap) #logN
            print(original)
    else:
        heapq.heappush(heap, (abs(x), x)) #logN