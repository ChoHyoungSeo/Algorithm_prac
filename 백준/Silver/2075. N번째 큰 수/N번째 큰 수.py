#그냥 구현: 메모리 초과.
#priority queue K개만 유지
#heapq

import heapq
n = int(input())
heap = []

for _ in range(n):
    numbers = map(int, input().split())
    for num in numbers:
        if len(heap) < n:
            heapq.heappush(heap, num)
        else:
            if heap[0] < num:
                heapq.heapreplace(heap, num)

print(heap[0]) #n개 중 가장 작은 수 = n번째로 큰 수