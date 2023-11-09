#euclidean algorithm

def gcd(a,b):
    while b > 0:
        a, b = b, a%b
    return a

def lcm(a, b):
    return a*b / gcd(a,b)
    
def solution(arr):
    std = 1
    for num in arr:
        std = lcm(num, std)
    
    return std