# 2 차원을 1차원으로
tot=int(input())

ans_list=[]
for i in range(tot):
    x,y = map(int,input().split())
    for a in range(y,y+10):
        for b in range(x,x+10):
            ans_list.append(a*100+b)
print(ans_list)
print(len(list(set(ans_list))))

#####
tot = int(input())
array = [[0] * 100 for _ in range(100)]

for _ in range(tot):
    x, y = map(int, input().split())
    for i in range(y, y+10):
        for j in range(x, x+10):
            array[i][j] = 1

result = 0
for i in range(100):
    result += array[i].count(1)

print(result)


