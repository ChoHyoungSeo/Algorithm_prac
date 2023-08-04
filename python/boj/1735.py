import math
a, b = map(int, input().split())
c, d = map(int, input().split())

up, down = (b*c+a*d), b*d
while math.gcd(up, down) != 1:
    std = math.gcd(up, down)
    up //= std
    down //= std
print(up, down)