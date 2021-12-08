def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for phone1, phone2 in zip(phoneBook, phoneBook[1:]):
        if phone2.startswith(phone1):
            return False
    return True

def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if len(phone_book[i]) < len(phone_book[i+1]):
            if phone_book[i + 1][:len(phone_book[i])] == phone_book[i]:
                answer = False
                break
    return answer

#test 20 -> 287
#     from collections import deque
# import copy
# def solution(phone_book):
#     answer = True
#     prefix_dict = {}
#     phone_book.sort(key = len)
#     phone_book = deque(phone_book)
#     st = phone_book[0]
#     for num in copy.deepcopy(phone_book):
#         try:
#             if num == st:
#                 pass
#             k = phone_book[0]
#             phone_book.popleft()
#             prefix_dict[num] = num[:len(k)+1]
#             for key, val in prefix_dict.items():
#                 if val in phone_book[0]:
#                 # if phone_book[0].startswith(val):
#                     answer = False
#                     break
#         except:
#             break
#     return answer


"""
test20 480
from collections import deque
import copy
def solution(phone_book):
    answer = True
    answer = True
    prefix_dict = {}
    phone_book.sort(key = len)
    phone_book = deque(phone_book)
    st = phone_book[0]
    for num in copy.deepcopy(phone_book):
        try:
            if num == st:
                pass
            k = phone_book[0]
            phone_book.popleft()
            prefix_dict[num] = num[:len(k)+1]
            for key, val in prefix_dict.items():
                if phone_book[0].startswith(val):
                    answer = False
                    break
        except:
            break
    return answer"""

#test20 675
# from collections import deque
# import copy
# phone_book = ["123", "456", "789"]
# answer = True
# prefix_dict = {}
# phone_book.sort(key = len)
# phone_book = deque(phone_book)
# st = phone_book[0]
# for num in copy.deepcopy(phone_book):
#     try:
#         if num == st:
#             pass
#         samp = []
#         k = phone_book[0]
#         phone_book.popleft()
#         prefix_dict[num] = num[:len(k)+1]
#         print(samp)
#         print(phone_book)
#         print(prefix_dict)
#         for key, val in prefix_dict.items():
#             samp.append(val)
#             # if k in samp:
#             #     answer = False
#             if phone_book[0].startswith(val):
#                 answer = False
#                 break
#     except:
#         break
# print(answer)

"""
정확도 만점, 효율성 0점 (test20 877)
def solution(phone_book):
    answer = True
    phone_book.sort(key = len)
    i = 0
    while True:
        for num in phone_book:
            std = phone_book[i]
            if num.startswith(std) and num != std:
                answer = False
                break
        if i == len(phone_book)-1:
            break
        i += 1
    return answer"""

"""
정확도 만점
효율성 50점 (test 20 464)
from collections import deque
import copy
def solution(phone_book):
    answer = True
    prefix_dict = {}
    phone_book.sort(key = len)
    phone_book = deque(phone_book)
    for num in copy.deepcopy(phone_book):
        try:
            k = len(phone_book[0])
            phone_book.popleft()
            prefix_dict[num] = num[:k+1]
            for key, val in prefix_dict.items():
                if phone_book[0].startswith(val):
                    answer = False
                    break
        except:
            break
    return answer
    """
