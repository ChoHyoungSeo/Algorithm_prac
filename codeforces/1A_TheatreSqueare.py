import sys
import math

ans = row = col = 0
n,m,a = map(int, sys.stdin.readline().split())
if n*m <= a*a:
  ans =1
else:
  row += math.ceil(n/a)
  col += math.ceil(m/a)
  ans = row*col

print(ans)