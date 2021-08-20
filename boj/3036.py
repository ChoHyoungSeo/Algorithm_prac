def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

if __name__ == '__main__':
    rings = int(input())
    rad = list(map(int, input().split()))
    std = rad[0]
    for i in range(1, rings):
        div = gcd(std, rad[i])
        print("%d/%d" %((std/div), (rad[i]/div)))

