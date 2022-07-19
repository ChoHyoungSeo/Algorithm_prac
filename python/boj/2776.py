Tcase = int(input())
for _ in range(Tcase):
    _ = int(input())
    stdNums = set(map(int, input().split())) #이거를 list로 받으면 시간초과가 나네,,
    _ = int(input())
    testNums = list(map(int, input().split()))

    for num in testNums:
        if num in stdNums:
            print(1)
        else:
            print(0)