from collections import deque

num = int(input())
nums = deque(i+1 for i in range(num))
ans = []

while nums:
    try:
        ans.append(nums.popleft())
        nums.append(nums.popleft())
    except:
        break

for i in range(len(ans)):
    print(ans[i], end=' ')
