#9093
a = int(input())
tmp = []
for i in range(a):
    tmp.append(input().split())
    for j in tmp[len(tmp)-1]:
        print(j[::-1], end=" ")

    tmp = []