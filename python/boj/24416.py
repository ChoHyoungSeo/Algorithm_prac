cnt = 0
def fibonacci(n):
    global cnt
    f = [1] * (n + 1)
    for i in range(3, n + 1):
        cnt += 1
        f[i] = f[i-1] + f[i-2]
    return f[n]

if __name__ == '__main__':
    N = int(input())
    print(fibonacci(N), cnt)