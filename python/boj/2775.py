def pnum(a:int, b:int) -> int:
    if a == 0:
        return b
    if b == 1:
        return 1
    else:
        return pnum(a, b-1) + pnum(a-1, b)

if __name__ == '__main__':
    q = int(input())

    for i in range(q):
        r = int(input())
        w = int(input())

        print(pnum(r,w))