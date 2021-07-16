def num(a: int) -> None:
    for i in range(2,a+1):
        if a % i == 0:
            print(i)
        else:
            continue
        return num(a//i)

if __name__ == '__main__':
    num(int(input()))