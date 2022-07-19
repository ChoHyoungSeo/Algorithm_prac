a = int(input())
s = 1
tot = 0
ans = 0

if a == 1:
    print("1/1")

else:
    for i in range(2,10000000):
        if a <= s+i:
            tot = i  #5
            break
        else:
            s += i
            continue

    for i in range(1, tot+1):
        ans += i #총갯수

    if tot % 2 == 0 :
        print("%d/%d" %((tot - ans + a), (ans - a + 1)))
    else:
        print("%d/%d" %((ans - a + 1),(tot - ans + a)))