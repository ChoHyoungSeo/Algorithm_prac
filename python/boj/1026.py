#1026
_ = int(input())
a_nums = sorted(list(map(int, input().split())), reverse=True)
b_nums = list(map(int, input().split()))
num_dict = {}
tmp = sorted(b_nums)
ans = 0
#dictionary를 사용한 경우 중복되는 값이 들어가지를 않네
#list를 이용할가 했지만 이게 더 빠른 방법일듯
#dictionary가 중첩이 안되니 아래 다른 for 문돌리지 말고 nesting 하게 한번에
for num in b_nums:
    num_dict[num] = tmp.index(num)
    tmp[tmp.index(num)] = -1
    ans += num * a_nums[num_dict[num]]

    # for i in range(len(b_nums)):
        # ans += b_nums[i] * a_nums[num_dict[b_nums[i]]]
        # del b_nums[i]

print(ans)


import sys

N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

A.sort()
B.sort(reverse=True)

ans = 0
for i in range(len(A)):
    ans += (A[i] * B[i])

print(ans)

_ = int(input())
a_nums = sorted(list(map(int, input().split())), reverse=True)
b_nums = list(map(int, input().split()))
num_dict = {}
tmp = sorted(b_nums)
ans = 0

for num in b_nums:
    num_dict[num] = tmp.index(num)
    tmp[tmp.index(num)] = -1
    ans += num * a_nums[num_dict[num]]

print(ans)