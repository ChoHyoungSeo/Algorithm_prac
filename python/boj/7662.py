import sys
input = sys.stdin.readline
import heapq

def pop(heap):
    #처음 삭제하는 원소라면 delete 되었다고 알려주기
    while heap:
        data, id = heapq.heappop(heap)
        if not deleted[id]:
            deleted[id] = True
            return data
    return None

for _ in range(int(input())):
    k = int(input())
    min_heap = []
    max_heap = [] #값을 음수 부호로 붙이기
    id = 0
    deleted = [False] * (k+1)
    for i in range(k):
        command = input().split()
        operator, data = command[0], int(command[1])
        if operator == 'D':
            if data == -1:
                pop(min_heap)
            elif data == 1:
                pop(max_heap)
        elif operator == "I":
            heapq.heappush(min_heap, (data, id))
            heapq.heappush(max_heap,(-data, id))
            id += 1
    max_value = pop(max_heap)
    if max_value == None:
        print("EMPTY")
    else:
        #pop을 구현해서 min heap에서도 제거되기 때문에 넣어주기
        heapq.heappush(min_heap, (-max_value, id))
        print(-max_value, pop(min_heap))
