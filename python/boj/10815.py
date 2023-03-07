# timeout
# _ = int(input())
# my_num = list(map(int, input().split()))
# _ = int(input())
# target_num = list(map(int, input().split()))
# ans = []
# for num in target_num:
#     if num in my_num:
#         ans.append(1)
#     else:
#         ans.append(0)
# print(*ans)

# answer
_ = int(input())
my_set = set(map(int, input().split()))
_ = int(input())
target_list = list(map(int, input().split()))
ans = []
std = set(target_list) - my_set
for num in target_list:
    if num in std:
        ans.append(0)
    else:
        ans.append(1)
print(*ans)