n = int(input())
trees = []
for _ in range(n):
    trees.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(len(trees[i])):
        if j == 0:
            trees[i][j] += trees[i-1][j]
        elif j == len(trees[i]) - 1:
            trees[i][j] += trees[i-1][j-1]
        else:
            trees[i][j] += max(trees[i-1][j-1], trees[i-1][j])
print(max(trees[-1]))