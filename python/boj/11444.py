#using DP, memory error
# a = int(input())
# nums = [0, 1]
# if a < 2:
#     print(nums[a])

# for i in range(2, a+1):
#     nums.append(nums[i-1]+nums[i-2])
# print(nums[-1]%1000000007)

#### Time out
# from collections import deque
# import sys
# num = int(input())
# nums = deque([0,1])
# for i in range(2, num+1):
#     nums.append(nums.popleft() + nums[0])
    
# print(nums[-1]%1000000007)

### mem
# d = [0]* 1000
# def fib(x):
#     if x == 1 or x== 2:
#         return 1
#     if d[x] != 0:
#         return d[x]
#     d[x] = fib(x-1)+ fib(x-2)
#     return d[x]

#use matmul.
N = int(input())
matrix = [[1, 1], [1, 0]]

# 행렬 곱셈
def mul_matrix(mat1, mat2):
    res = [[0]*2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for z in range(2):
                res[i][j] += mat1[i][z] * mat2[z][j] % 1000000007
    return res

# divide and conquer
def power(a, b):
    if b == 1:
        return a
    else:
        tmp = power(a, b // 2)
        if b % 2 == 0:
            return mul_matrix(tmp, tmp)
        else:
            return mul_matrix(mul_matrix(tmp, tmp), a)
result = power(matrix, N)

print(result[0][1] % 1000000007)