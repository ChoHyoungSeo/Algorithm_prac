# boj 1417번

# n = int(input())
# std = int(input())

# if n <= 1 :
#   print(0)

# else :
#   nums = []
#   for _ in range(n-1) :
#     nums.append(int(input()))

#   ans = 0
#   while max(nums) >= std:
#     tar = nums.index(max(nums))
#     std += 1
#     nums[tar] -=1
#     ans += 1

#   print(ans)

#heap을 활용해서도 해결할수 있다
import sys, heapq
input = sys.stdin.readline

n = int(input())
win = int(input())
nums = []

for _ in range(n - 1):
    num = int(input())
    heapq.heappush(nums, (-num, num))

cnt = 0
while nums:
    num = heapq.heappop(nums)[1]
    if num >= win:
        num -= 1
        win += 1
        cnt += 1
        heapq.heappush(nums, (-num, num))

print(cnt)