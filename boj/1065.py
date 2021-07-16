# oop st
def hanNum(a:int) -> int:
    cnt = 0
    for i in range(1, a+1, 1):
        if i < 100 :
            cnt += 1

        elif i >= 100 and i < 1000 :
            w = i // 100
            x = (i - (w * 100)) // 10
            y = i - (w * 100) - (x * 10)

            if w - x == x - y :
                cnt += 1

            else:
                continue
        else:
            continue

    return cnt

if __name__ == '__main__':
    print(hanNum(int(input())))