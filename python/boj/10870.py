#recursion
def fib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

if __name__ == '__main__':
    print(fib(int(input())))
    
#================================
#iterationdef
# fib02(n):
#     if n == 0:
#         print(0)
#     elif n == 1:
#         print(1)
#     else:
#         a = 0
#         b = 1
#         for i in range(2,n+1):
#             c = a+b
#             a = b
#             b = c
#         print(c)
