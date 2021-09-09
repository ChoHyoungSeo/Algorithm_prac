a = int(input())

for _ in range(a):
    x, y = map(int, input().split())
    tot = y - x
    cnt = 0
    gap = 1
    loc = 0
    while loc < tot :
        cnt += 1
        loc += gap
        if cnt % 2 == 0 :
            gap += 1
    print(cnt)