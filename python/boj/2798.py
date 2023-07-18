# import sys

# numCard, target = map(int, sys.stdin.readline().rstrip().split())
# card = list(map(int, sys.stdin.readline().rstrip().split()))
# card.sort()
# ans = []

# for i in range(numCard):
#     for j in range(i+1, numCard):
#         for k in range(j+1, numCard):
#             if card[i] + card[j] + card[k] > target:
#                 continue
#             else:
#                 ans.append(card[i] + card[j] + card[k])

# ans.sort()
# print(ans[-1])

#using combination
from itertools import combinations

N, M = map(int, input().split())
lst = list(map(int, input().split()))
ans = []

for comb in combinations(lst, 3):
    if sum(comb) > M:
        continue
    else:
        ans.append(sum(comb))
print(max(ans))