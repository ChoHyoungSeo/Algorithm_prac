# n개를 3번에 옮기는 것은
# n-1개를 2번에 옮기는 것이다 + 마지막한개 바로 목적지
# 1 3 7 2 ^ n - 1
def hanoi(n, startp, endp, middlep):
    if n == 1:
        print(startp, endp)
    else:
        hanoi(n-1, startp, middlep, endp)
        print(startp, endp)
        hanoi(n-1, middlep, endp, startp)

if __name__ == '__main__':
    k = int(input())
    print((2 ** k) - 1)
    hanoi(k, 1, 3, 2)