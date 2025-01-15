#circular/doubly linked list 스타일로 구현해봐도 재미있을 듯.
from collections import deque

_ = int(input())
nums = list(map(int, input().split()))
queue = deque((idx+1, num) for idx, num in enumerate(nums))
idx, cur = queue.popleft()
ans = [idx] #index 번호

for _ in range(len(nums)-1):
    if cur > 0:
        for _ in range(cur-1):
            queue.append(queue.popleft())
    else:
        for _ in range(-cur):
            queue.appendleft(queue.pop())
    idx, cur = queue.popleft()
    ans.append(idx)

print(*ans)