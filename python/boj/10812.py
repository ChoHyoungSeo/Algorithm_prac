tot, chance = map(int, input().split())
nums = [x for x in range(1, tot+1)]

for _ in range(chance):
  start, end, std = map(int, input().split())
  tmp = nums[start-1:end-1]
  head = nums[start-1:std-1]
  tail = nums[std-1:end]
  nums[start-1:end] = tail+head
print(*nums)