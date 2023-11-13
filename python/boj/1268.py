tot = int(input())
students = []
std = [0]*tot
for i in range(tot):
    students.append(list(map(int, input().split())))
    std[i] = [0]*tot
for i in range(5):
    for j in range(tot):
        for k in range(j+1, tot):
            if students[j][i] == students[k][i]:
                std[k][j] = 1
                std[j][k] = 1
cnt = []
for student in std:
    cnt.append(sum(student))
print(cnt.index(max(cnt))+1)