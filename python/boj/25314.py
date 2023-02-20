a = int(input())
if a % 4 == 0:
  std = int(a // 4)
else:
  std = int(a//4) + 1

ans = "long "
print(ans * std + "int")