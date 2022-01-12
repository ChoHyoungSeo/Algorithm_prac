#2475
nums = list(map(int, input().split()))
tmp = 0

for num in nums:
    tmp += num**2

print(tmp%10)