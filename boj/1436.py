a = int(input())
num = 0
cnt = 0

while True:
    num += 1
    if '666' in str(num):
        cnt += 1
    else:
        continue
    if cnt == a:
        print(num)
        break