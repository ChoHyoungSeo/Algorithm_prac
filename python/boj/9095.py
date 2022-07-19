#9095

def ans(a):
    if a == 1:
        return 1
    elif a == 2:
        return 2
    elif a == 3:
        return 4
    else:
        return ans(a-1) + ans(a-2) + ans(a-3)

if __name__ == '__main__':
    tot = int(input())
    for _ in range(tot):
        a = int(input())
        print(ans(a))