# n = int(input())
# arr = list(map(int, input().split()))
# stack = []
# NGE = [-1] * n

# for i in range(n):
#     x = arr[i]
#     if len(stack) == 0 or stack[-1][0] >= x:
#         stack.append((x,i)) #(수, idx) 내림차순 일 때 넣어주기
#     else:
#         while len(stack) > 0: #역방향 꺼내기
#             previous, idx = stack.pop()
#             if previous >= x:
#                 stack.append((previous, idx))
#                 break
#             else:
#                 NGE[idx] = x #오큰수 기록
#         stack.append((x,i))
# for x in NGE:
#     print(x, end = ' ')

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
