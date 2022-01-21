#1475
import math
nums = list(map(int, input()))
tmp = [0]*10

for num in nums:
    tmp[num] += 1

if tmp.index(max(tmp)) == 6 or tmp.index(max(tmp)) == 9:
    tmp[6], tmp[9] = math.ceil((tmp[6] + tmp[9]) / 2), math.ceil((tmp[6] + tmp[9]) / 2)

print(int(max(tmp)))