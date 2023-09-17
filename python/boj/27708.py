T = int(input())
print(T)
print()

for _ in range(T):
    input()
    N = int(input())
    arr = list(map(int, input().split()))

    arr.sort()

    arr[0], arr[1] = arr[1], arr[0]

    print(N)
    print(" ".join(map(str, arr)))
    print()
