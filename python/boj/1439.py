# from collections import Counter

# nums = list(map(int, input()))
# nums_dict = Counter(nums)
# # tar = nums_dict[min(nums_dict.values())] #0 1
# tmp = []
# tick = 0
# cnt = 0

# for key, value in nums_dict.items():
#     if min(nums_dict.values()) == value:
#         tar = key

# if min(nums_dict.values()) == len(nums):
#     print(0)
# else:
#     for idx, num in enumerate(nums):
#         if num == tar:
#             tmp.append(idx)

#     for i in range(len(tmp)-1):
#         if tmp[i+1] - tmp[i] == 1:
#             if tick == 1:
#                 continue
#             else:
#                 tick = 1
#                 cnt += 1

#         else:
#             tick = 0
#             cnt += 1
#     print(cnt)

#완전히 문제를 안읽었네,, 이방법이 아니야

# nums = list(map(int, input()))
# cnt = 0
# tick = 0

# for i in range(len(nums)-1):
#     if nums[i] != nums[i+1]:
#         tick = 1
#     else:
#         if tick == 1:
#             tick = 0
#         else:
#             continue

#     if tick == 1:
#         cnt += 1

# if cnt % 2 == 0:
#     print(cnt//2)
# elif cnt == 0 or cnt == 1:
#     print(cnt)
# else:
#     print((cnt - 1)//2 + 1)

#즉,
nums = list(map(int, input()))
cnt = 0

for i in range(len(nums)-1) :
    if nums[i] != nums[i+1]:
        cnt += 1

print((cnt+1)//2)