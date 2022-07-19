a, b = map(int, input().split())
tot = a*b
nums = list(map(int, input().split()))

for num in nums:
    print(num-tot, end=" ")