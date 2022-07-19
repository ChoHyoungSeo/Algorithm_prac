import sys

_ = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip().split()))
ans = [-1 for x in range(len(nums))]
stack = [0]

for i in range(1,len(nums)):
    while stack and nums[stack[-1]] < nums[i]:
        ans[stack.pop()] = nums[i]

    stack.append(i)

print(*ans)
