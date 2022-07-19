# 1009번
# #100만 square power
# #그걸 다시 input 수만큼 도니까 input이 4만 돼도
# 제한시간 1초 400만번 이상의 연산이 일어나 -> 시간초과

# n = int(input())

# for i in range(n):
#     num, square = map(int,input().split())
#     tmp = 1

#     for j in range(1, square+1):
#         tmp = int(str(tmp * num)[-1])

#     if tmp == 0:
#         print(10)
#     else:
#         print(tmp)


# #패턴을 찾아야해

import sys

n = int(sys.stdin.readline().strip())

for i in range(n):
    num, square = map(int, sys.stdin.readline().strip().split())
    key = int(str(num)[-1])

    # 1개 반복
    if key in [1, 5, 6]:
        print(key)

    # 0은 10
    elif key == 0:
        print(10)

    # 2개 반복 홀수면 자신
    elif key in [4, 9]:
        if square % 2 == 0 and key == 4:
            print(6)
        elif square % 2 == 0 and key == 9:
            print(1)
        else:
            print(key)

    # 4개 반복
    else:
        if square % 4 == 0:
            if key == 2 or key == 8:
                print(6)
            else:
                print(1)

        elif square % 4 == 3:
            if key == 2:
                print(8)
            elif key == 3:
                print(7)
            elif key == 7:
                print(3)
            else:
                print(2)

        elif square % 4 == 2:
            if key == 2 or key == 8:
                print(4)
            else:
                print(9)
        else:
            print(key)