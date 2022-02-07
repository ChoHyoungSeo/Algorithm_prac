#2576
nums = []

for _ in range(7):
    tmp = int(input())
    if tmp % 2 != 0 :
        nums.append(tmp)
    else:
        continue

if not nums:
    print(-1)

else:
    print(sum(nums))
    print(sorted(nums)[0])