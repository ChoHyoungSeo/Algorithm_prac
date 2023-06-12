# from collections import Counter
# def solution(array):
#     answer = 0
#     # cnt_dict = Counter(array)
#     ans = Counter(array).most_common()
#     try:
#         if ans[0][-1] == ans[1][-1]:
#             return -1
#     except:
#         pass
#     return ans[0][0]

def solution(array):
    nums = [0 for x in range(max(array)+1)]
    rep = 0
    
    for num in array:
        nums[num] += 1
    std = max(nums)

    for num in nums:
        if num == std:
            rep += 1
    if rep > 1:
        return -1
    else:
        return nums.index(std)