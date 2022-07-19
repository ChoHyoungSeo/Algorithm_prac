a,b = map(int,input().split())
def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(int(factorial(a)/(factorial(b)*factorial(int(a-b)))))