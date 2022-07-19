num = int(input())
cnt = 0
tmp = num

while(True):
    cnt += 1
    a = num // 10
    b = num - (a * 10)
    num = b*10 + ((a+b)%10)
    if num == tmp:
        break
    else:
        continue

print(cnt)