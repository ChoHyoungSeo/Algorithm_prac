import sys
input = sys.stdin.readline

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
    
while True:
    ans = 0
    num = input().strip()
    if int(num) == 0:
        break
    for i in range(len(num)):
        ans += int(num[len(num)-i-1]) * factorial(i+1)
    print(ans)


# lambda식 사용
import sys

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

while True:
    num = sys.stdin.readline().strip()
    if int(num) == 0:
        break    
    n = len(num)
    print(sum(map(lambda x : int(num[x])*factorial(n-x), range(n))))