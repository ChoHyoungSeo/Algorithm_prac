import math

def lcm(n,m):
    return n*m // math.gcd(n,m)

def solution(n, m):
    answer = []
    answer.append(math.gcd(n,m))
    answer.append(lcm(n,m))
    return answer

# lcm method can be used in python version 3.11 or above
# programmers: 3.9.x