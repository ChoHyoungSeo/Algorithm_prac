#2480
a, b, c = map(int, input().split())
# 10,000원+(같은 눈)×1,000
if a == b and b == c:
    print(10000 + a * 1000)
# 1,000원+(같은 눈)×100
elif (a == b and b != c) or (a != b and b == c) or (a == c and a != b):
    if a == b:
        print(1000 + a * 100)
    elif b == c:
        print(1000 + c * 100)
    else:
        print(1000 + c * 100)

else:
    print(max(a,b,c) * 100)