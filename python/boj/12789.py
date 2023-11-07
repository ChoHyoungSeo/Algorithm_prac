from collections import deque
n = int(input())
nums = deque(list(map(int, input().split())))
stack = []
target = 1

while nums:
    if nums[0] == target:
        nums.popleft()
        target += 1
    else:
        stack.append(nums.popleft())

    while stack:
        if stack[-1] == target:
            stack.pop()
            target += 1
        else:
            break
print('Nice' if not stack else 'Sad')