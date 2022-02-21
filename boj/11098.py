tot=int(input())
for i in range(tot):
    pDict={}
    pnum = int(input())
    for j in range(pnum):
        a,b = input().split()
        a = int(a)
        pDict[a] = b
    print(pDict[max(pDict)])