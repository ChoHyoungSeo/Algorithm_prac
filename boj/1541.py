#- 기준으로
nums = input().split('-')
num_list = []
for num in nums:
    ans = 0
    sp_num = num.split('+')
    for j in sp_num:
        ans += int(j)
    num_list.append(ans)
part_num = num_list[0]
for i in range(1, len(num_list)):
    part_num -= num_list[i]
print(part_num)