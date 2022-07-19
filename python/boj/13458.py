#13458
import math

tot_class = int(input())
tot_people = list(map(int, input().split()))
tot_num, vice_num = map(int, input().split())
ans = 0

for num in tot_people:
    num -= tot_num
    if num <= 0:
        continue
    else:
        num = math.ceil(num/vice_num)
        ans += num

print(ans + tot_class)