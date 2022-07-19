a = int(input())
cnt = 0

while True:
    if a < 0:
        cnt = -1
        break
    elif a % 5 == 0:
        cnt += a // 5
        break

    else :
        a -= 3
        cnt += 1

print(cnt)