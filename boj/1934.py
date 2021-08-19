#using euclidean
def gcd(a: int, b: int) -> int:
    while b > 0 :
        a, b = b, a%b
    return a

def lcm(a: int, b: int) -> int:
    return a*b // gcd(a,b)

if __name__ == '__main__':
    a = int(input())

    for i in range(a):
        a, b = map(int, input().split())
        print(lcm(a,b))