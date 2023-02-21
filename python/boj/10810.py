balls, tries = map(int, input().split())
nums = [0 for x in range(balls)]
for _ in range(tries):
  begin, end, target = map(int, input().split())
  nums[begin-1:end] = [target for x in range(end-begin+1)]
print(*nums)