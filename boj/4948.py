# while True:
#     a = int(input())
#     ans = []
#     if a == 0:
#         break
#     for i in range(a+1, 2*a+1):
#         cnt = 0
#         for j in range(2,int(i**0.5)+1):
#             if i % j == 0:
#                 cnt += 1
#             if cnt > 1:
#                 break
#             else:
#                 continue
#         if cnt == 0:
#             ans.append(i)
#     print(len(ans))

# timeout을 막기위해선 문제에 나온 범위의 소수를 미리 다 찾아놓고 문제를 풀어야 한단
import math
import sys

def num(num):     #소수 구하는 함수 (3 5 7 11 ...)
    if num == 1:  #1은 소수가 아니다.
        return False
    else :
        for i in range(2,int(math.sqrt(num))+1) :
            if num%i == 0:
                return False
        return True

all_list = list(range(2,246912)) # 문제에서 주어진 범위
save_list=[]

for i in all_list : # 주어진 범위 안의 소수들을 찾아서 저장해놓는다.
    if num(i):
        save_list.append(i)

num = int(sys.stdin.readline())

while num != 0:
    count = 0
    for i in save_list:
        if num < i <= num*2:
            count += 1
    print(count)
    num = int(sys.stdin.readline())