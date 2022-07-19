# 10816
#time over
# tot = int(input())
# nums = list(map(int, input().split()))
# _ = int(input())
# tmp = list(map(int, input().split()))
# ans = []

# for num in tmp: 
#     ans.append(nums.count(num)) 중첩되네

# for i in range(len(ans)):
#     print(ans[i], end = ' ')

tot = int(input())
nums = list(map(int, input().split()))
_ = int(input())
target = list(map(int, input().split()))
tmp={}

for num in nums:
    tmp[num] = 0

for num in nums:
    tmp[num] += 1

for num in target:
    try:
        print(tmp[num], end = " ")
    except:
        print(0, end=" ")