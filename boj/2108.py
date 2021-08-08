from collections import Counter
import sys
a = int(sys.stdin.readline().strip())
nums = []

for _ in range(a):
    nums.append(int(sys.stdin.readline().strip()))
nums.sort()

mod = Counter(nums).most_common()

if len(mod) > 1:
    if mod[0][1] == mod[1][1]:
        mod_ans = mod[1][0]
    else:
        mod_ans = mod[0][0]
else:
    mod_ans = mod[0][0]

print(round(sum(nums)/len(nums)))
print(nums[int((a-1)/2)])
print(mod_ans)
print(max(nums)-min(nums))
#Counter() 하면 전체, Counter(2)는 많은거 2개 이런식 숫자 횟수 튜플로 반환해준다
############################################################
""" timeover
import sys

a = int(sys.stdin.readline().strip())
nums = []
nums_dict={}
med_nums = []
for i in range(a):
    nums.append(int(sys.stdin.readline().strip()))

nums.sort()

for i in nums:
    nums_dict[i] = nums.count(i)    여기서 timecomplexity를 잡아먹는가

for key, value in nums_dict.items():
    if value == max(nums_dict.values()):
        med_nums.append(key)

if len(med_nums) == 1:
    med = med_nums[0]
else:
    med = sorted(med_nums)[1]

print("%d" %(round(sum(nums)/len(nums))))
print(nums[(int(a/2))])
print(med)
print(max(nums) - min(nums)) """

############################################################

""" 이건 pypy로 성공이 나온다.. Counter 없이 답이 나오긴 했지만
맞춰 풀어야하는건가 흠,,
a = int(input())
l = []
tmp = {}
ans = []
m = 0

for _ in range(a):
    l.append(int(input()))

print(round(sum(l)/len(l)))
print(sorted(l)[int(len(l)/2)])

for i in l:
    tmp[i] = 0

for i in l:
    tmp[i] += 1

for value in tmp.values():
    if value > m:
        m = value

for key, value in tmp.items(): 
    if value == m:
        ans.append(key)

if len(ans) == 1:
    print(ans[0])
else:
    print(sorted(ans)[1])

print(max(l)-min(l)) """