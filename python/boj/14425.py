a, b = map(int, input().split())
target = set()
pool = []
ans = 0

for i in range(a):
  target.add(input())
for i in range(b):
  pool.append(input())

for inp in pool:
  if inp in target:
    ans += 1
print(ans)