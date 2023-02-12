# boj 2738.py
# boj does not support numpy package

a, b = map(int, input().split())
mat_a = []
mat_b = []
ans = []

for i in range(a):
  tmp = list(map(int, input().split()))
  mat_a.append(tmp)
  
for i in range(a):
  tmp = list(map(int, input().split()))
  mat_b.append(tmp)

for x_list, y_list in zip(mat_a, mat_b):
  tmp = []
  for x, y in zip(x_list, y_list):
    tmp.append(x+y)
  ans.append(tmp)
  
for nums in ans:
  print(*nums, end='\n')
