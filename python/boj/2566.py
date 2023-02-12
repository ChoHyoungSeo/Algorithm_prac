ans = 0
ans_idx01 = 0
ans_idx02 = 0

for i in range(9):
  tmp = list(map(int, input().split()))
  if max(tmp) > ans:
    ans_idx01 = i
    ans_idx02 = tmp.index(max(tmp))
    ans = max(tmp)

print(ans)
print(ans_idx01 + 1, ans_idx02+1)