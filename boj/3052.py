num = [0 for _ in range(42)]
cnt = 0

for i in range(10):
    num[int(input())%42] += 1

for i in range(len(num)):
    if num[i] != 0:
        cnt += 1
print(cnt)