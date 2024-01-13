# import math
# def solution(nums):
#     answer = 0
#     for i in range(len(nums)-2):
#         for j in range(i+1, len(nums)-1):
#             for k in range(j+1, len(nums)):
#                 flag=False
#                 num = nums[i] + nums[j] + nums[k]
#                 for l in range(2, int(math.sqrt(num))+1):
#                     if num % l == 0:
#                         flag = True
#                         break
#                 if not flag:
#                     answer += 1
#     return answer
# # import math

# # def is_prime(num):
# #     if num < 2:
# #         return False
# #     for i in range(2, int(math.sqrt(num)) + 1):
# #         if num % i == 0:
# #             return False
# #     return True

# # def solution(nums):
# #     answer = 0
# #     n = len(nums)

# #     for i in range(n - 2):
# #         for j in range(i + 1, n - 1):
# #             for k in range(j + 1, n):
# #                 triplet_sum = nums[i] + nums[j] + nums[k]
# #                 if is_prime(triplet_sum):
# #                     answer += 1

# #     return answer

from itertools import combinations
def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    
    sqrt_num = int(num**0.5) + 1
    for i in range(3, sqrt_num, 2):
        if num % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    result_list = [sum(combination) for combination in combinations(nums, 3)]
    for num in result_list:
        if is_prime(num):
            answer += 1
    return answer