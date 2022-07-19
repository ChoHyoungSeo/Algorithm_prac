#2748
# 재귀는 시간초과

# def fib(a):
#     if a == 0:
#         return 0
#     elif a == 1:
#         return 1
    
#     else:
#         return fib(a-1) + fib(a-2)

# if __name__ == '__main__':
#     print(fib(int(input())))


n = int(input())
# 자연수라는 조건, 0은 제외
if n == 1:
    print(1)

else: 
    a = 0
    b = 1

    for i in range(2, n+1):
        c = a + b
        a = b
        b = c
        
    print(c)
