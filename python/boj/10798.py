a = list(input())
b = list(input())
c = list(input())
d = list(input())
e = list(input())
ans = []

for i in range(max(len(a), len(b), len(c), len(d), len(e))):
  try:
    ans.append(a[i])
  except:
    pass
  try:
    ans.append(b[i])
  except:
    pass
  try:
    ans.append(c[i])
  except:
    pass
  try:
    ans.append(d[i])
  except:
    pass
  try:
    ans.append(e[i])
  except:
    pass
for i in range(len(ans)):
  print(ans[i],end="")