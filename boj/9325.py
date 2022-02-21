#9325
tot = int(input())

for _ in range(tot):
    car = int(input())
    opNum = int(input())
    cnt = 0

    for i in range(opNum):
        p,q = map(int, input().split())
        cnt += p * q
    print(car + cnt)