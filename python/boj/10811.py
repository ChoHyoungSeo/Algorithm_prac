_, chance = map(int, input().split())
nums = [x for x in range(tot+1)]

for _ in range(chance):
  start, end = map(int, input().split())
  target = nums[start:end+1]
  nums[start:end+1] = target[::-1]
print(*nums[1:])