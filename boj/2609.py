#유클리드 호제법
a, b = map(int, input().split())

def gcd(a :int, b: int) -> int:
    while b > 0:
        a, b = b, a%b
    return a

def lcm(a: int, b: int) -> int:
    return a * b // gcd(a,b)

if __name__ == '__main__':
    print(gcd(a, b))
    print(lcm(a, b))

#python 3.9 이상부터는 내장함수로 있다

# import math
# a,b = map(int, input().split())
# print(math.gcd(a,b))
# print(math.lcm(a,b))