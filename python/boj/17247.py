import sys
input = sys.stdin.readline

height, weight = map(int, input().split())

target1 = []
target2 = []
ans = 0
for i in range(height):
    nums=list(map(int, input().split()))
    if 1 in nums:
        if target1:
            target2.append(i+1)
            target2.append(nums.index(1)+1)
        else:
            target1.append(i+1)
            target1.append(nums.index(1)+1)
for num1, num2 in zip(target1, target2):
    ans += abs(num1 - num2)
print(ans)