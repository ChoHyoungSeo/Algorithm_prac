a = int(input())
nums = []

for i in range(a):
    nums.append(list(map(int, input().split())))

for i in range(a):
    print("Case #%d: %d + %d = %d" %(i+1, nums[i][0], nums[i][1], nums[i][0] + nums[i][1]))