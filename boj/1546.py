num = int(input())
score = list(map(int, input().split()))
score.sort()
std = score[-1]

for i in range(num):
    score[i] = (score[i]/std) * 100

print(sum(score)/len(score))