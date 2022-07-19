a = int(input())
mul = 1
cnt = 0
for i in range(1,a+1):
    mul *= i

mul02 = str(mul)[::-1]
for i in range(len(mul02)):
    if mul02[i] == '0':
        cnt += 1
    else:
        break

print(cnt)