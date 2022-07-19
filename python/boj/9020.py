#에라토스테네스의 체,, 소수를 찾는 방법중 가장 효율적
# 찾고자 하는 수 까지 true로 채운 리스트를 이용 2를제외한 2의배수, 3을 제외한 3의 배수 5를 제외한 5의 배수,,, sqrt(n)까지 False로 바꾸면 2~n까지 숫자들 중 True 인 숫자들이 소수
import sys

def prime_list(n):
    sieve = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False
    return sieve
 
def gold(primes,n):
    index = 0
    while True:
        if primes[n//2-index] and primes[n//2+index]:
            return(n//2-index,n//2+index)
        index+=1

primes = prime_list(10001)

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    answer = gold(primes,n)
    print(answer[0],answer[1])