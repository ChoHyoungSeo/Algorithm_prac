tot = int(input())
for i in range(tot):
    _  = int(input())
    nums = list(map(int, input().split()))
    temp = []
    for num in nums:
        if num in temp:
            temp.remove(num)
        else:
            temp.append(num)
    print("Case #%d: %d" %((i+1), temp[0]))