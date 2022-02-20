#1267
_ = int(input())
pTime = list(map(int, input().split()))
yList = []
mList = []

for i in range(len(pTime)):
    yList.append(((pTime[i] // 30) + 1) * 10)
    mList.append(((pTime[i] // 60)+1)*15)

if sum(yList) > sum(mList):
    print("M", sum(mList))

elif sum(yList) < sum(mList):
    print("Y", sum(yList))
else:
    print("Y M",sum(mList))