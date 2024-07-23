def modular_exponentiation(A, B, C):
  if B == 0:
      return 1
  if B % 2 == 0:
      half = modular_exponentiation(A, B // 2, C)
      return (half * half) % C
  else:
      return (A * modular_exponentiation(A, B - 1, C)) % C

A, B, C = map(int, input().split())

result = modular_exponentiation(A, B, C)
print(result)
