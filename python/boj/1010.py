def factorial(n:int) -> int:
    if n == 1 or n==0:
        return 1
    else:
        return n*factorial(n-1)

if __name__ == '__main__':
    a = int(input())
    for _ in range(a):
        n,m = map(int, input().split())
        print("%d" %(factorial(m)/(factorial(n)*factorial(m-n))))
