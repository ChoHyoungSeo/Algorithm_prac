# # 중복되는 숫자의 개수를 알 수 없네
# def solution(X, Y):
#     answer = ''
#     nums = list(map(int, set(X) & set(Y)))
#     if not nums:
#         return '-1'
#     nums.sort(reverse=True)
#     return ''.join(list(map(str, nums)))

# # 시간초과
# def solution(X,Y):
#     nums = []
#     if not set(X) & set(Y):
#         return '-1'
#     Y = list(Y)
#     for num in X:
#         if num in Y:
#             nums.append(num)
#             Y.remove(num)
#     if set(nums) == {'0'}:
#         return '0'
#     return ''.join(sorted(nums, reverse=True))

from collections import Counter
def solution(X,Y):
    if not set(X) & set(Y):
        return '-1'
    X_dict = Counter(X)
    Y_dict = Counter(Y)
    total_dict = {}
    num = ''
    for key, val in X_dict.items():
        if key in Y_dict.keys():
            total_dict[key] = min(X_dict[key], Y_dict[key])
    if len(total_dict.keys()) == 1 and list(total_dict.keys())[0] == '0':
        return '0'
    for k, v in total_dict.items():
        word = k*int(v)
        num += word
    num = list(map(int, num))
    num.sort(reverse=True)
    return ''.join(list(map(str, num)))