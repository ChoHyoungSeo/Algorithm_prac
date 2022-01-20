# #에라토스테네스의 체 (백만까지)
# def prime_list(n):
#     #에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
#     sieve = [True] * n
#     #n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n) 까지 검사
#     m = int(n**0.5)

#     for i in range(2,m+1):
#         if sieve[i] == True: #i 가 소수인 경우
#             for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
#                 sieve[j] = False
#     #소수 목록 산출
#     return [i for i in range(2, n) if sieve[i] == True]

import math

# 소수 판별 함수(에라토스테네스의 체)
def is_prime_number(n):
    # 2부터 n까지의 모든 수에 대하여 소수 판별
    array = [True for i in range(n+1)] # 처음엔 모든 수가 소수(True)인 것으로 초기화(0과 1은 제외)

    # 에라토스테네스의 체
    for i in range(2, int(math.sqrt(n)) + 1): #2부터 n의 제곱근까지의 모든 수를 확인하며
        if array[i] == True: # i가 소수인 경우(남은 수인 경우)
            # i를 제외한 i의 모든 배수를 지우기
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1

    return [ i for i in range(2, n+1) if array[i] ]

# N이 1,000,000 이내로 주어지는 경우 활용할 것 => 이론상 400만번 정도 연산이고 메모리도 충분함

if __name__ == '__main__':
    year = int(input()) #이거보다 큰 소수
    prime_nums = is_prime_number(year)
    ans = 0
    if year == 1 or year == 2:
        ans = 6
    for i in range(len(prime_nums)):
        try:
            ans = prime_nums[i] * prime_nums[i+1]
            if ans > year:
                break
        except:
            break
print(ans)