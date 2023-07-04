# result = 0
# max_value = 0
# for i in range(5):
#     row = list(map(int, input().split()))
#     summary = sum(row)
#     if max_value < summary:
#         max_value = summary
#         result = i +1
# print(result, max_value)

nums = []
ans = []
for i in range(5):
    nums.append(list(map(int, input().split())))    

for idx, nums in enumerate(nums):
    ans.append((idx+1, sum(nums)))

ans.sort(key = lambda x: x[-1])
print(*ans[-1])