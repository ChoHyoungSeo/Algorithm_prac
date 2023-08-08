from itertools import permutations
n,m = map(int, input().split())
pool = [x for x in range(1,n+1)]
target = list(permutations(pool,m))

for nums in target:
    print(*nums)