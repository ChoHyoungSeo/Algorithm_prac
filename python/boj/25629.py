# _ = int(input())
# nums = list(map(int, input().split()))
# odd = []
# even = []
# for num in nums:
#     if num % 2 != 0:
#         odd.append(num)
#     else:
#         even.append(num)
# if len(nums) % 2 == 0:
#     if len(odd) == len(even):
#         print(1)
#     else:
#         print(0)
# else:
#     if len(odd) == len(even) + 1:
#         print(1)
#     else:
#         print(0)


# ###
# 입력을 받는다
N = int(input())
sequence = list(map(int, input().split()))

# 홀수와 짝수를 분리한다
odd_numbers = sorted([x for x in sequence if x % 2 == 1])
even_numbers = sorted([x for x in sequence if x % 2 == 0])

# 홀수와 짝수의 개수를 확인한다
num_odd = len(odd_numbers)
num_even = len(even_numbers)

# 홀수와 짝수의 개수에 따라 조건을 확인한다
if num_odd > N // 2 + N % 2 or num_even > N // 2:
    print(0)
else:
    print(1)
