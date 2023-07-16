import math
a, b = map(int, input().split())
print(math.lcm(a,b))


# def GCD(x,y):
#     while(y):
#         x, y = y, x%y
#     return x
# def LCM(x,y):
#     return (x*y)//GCD(x,y)