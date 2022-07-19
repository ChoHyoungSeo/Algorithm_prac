nums = []
idxDict = {}

for _ in range(9):        
    a = int(input())
    nums.append(a)

for idx, k in enumerate(nums):
    idxDict[k] = idx
ansIdx = idxDict[max(nums)]

print(max(nums))
print(ansIdx + 1)