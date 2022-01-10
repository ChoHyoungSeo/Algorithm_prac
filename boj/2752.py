#2752
nums = list(map(int, input().split()))

for i in range(len(nums)):
    print(sorted(nums)[i], end=' ')