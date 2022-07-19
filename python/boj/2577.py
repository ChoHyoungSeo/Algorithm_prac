a = int(input())
b = int(input())
c = int(input())
num = [0 for _ in range(10)]
std = str(a*b*c)

for i in range(len(std)):
    num[int(std[i])] += 1

for i in range(len(num)):
    print(num[i])