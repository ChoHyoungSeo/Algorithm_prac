#using euclidean
def gcd(a: int, b: int) -> int:
    while b > 0 :
        a, b = b, a%b
    return a

def lcm(a: int, b: int) -> int:
    return a*b // gcd(a,b)

if __name__ == '__main__':
    total = int(input())

    for _ in range(total):
        a, b = map(int, input().split())
        print(lcm(a,b))
