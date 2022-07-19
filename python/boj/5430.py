#첫번째 시간초과 input -> system 변환
#두번째 시간초과 list -> deque 연산
#이 방법은 안되겠다 중첩되네

# import sys
# from collections import deque

# tot = int(sys.stdin.readline().strip())
# func = ""
# nums = []
# tick = 0

# for i in range(tot):
#     func = sys.stdin.readline().strip() #.append(input())
#     _ = int(sys.stdin.readline().strip())
#     tmp = sys.stdin.readline().strip()
#     tmp = tmp[1:-1]
#     nums = deque(map(int, tmp.replace(',',' ').split()))
#     # nums = tmp #.append(tmp) #(list(map(int, tmp)))#.replace(',',''))))
#     # nums = deque(nums)

#     for i in range(len(func)):
#         if func[i] == 'R':
#             # nums = nums[::-1]
#             nums.reverse()  
#             print(nums)

#         else:
#             try:
#                 # del nums[0]
#                 nums.popleft()
#                 print(nums)
#             except:
#                 tick = 1
#                 print('error')
#                 break
#     if tick:
#         continue

#     else:
#         print(list(nums))


import sys
from collections import deque

tot = int(sys.stdin.readline().strip())

for i in range(tot):
    # func = []
    # nums = []
    numR = []
    func = deque(map(str, sys.stdin.readline().strip())) #.append(input())
    _ = int(sys.stdin.readline().strip())
    tmp = sys.stdin.readline().strip()
    tmp = tmp[1:-1]
    nums = deque(map(int, tmp.replace(',',' ').split()))
    cnt = 0
    ans = ''
    tick = 0

    for s_func in func:
        if s_func == "D":
            # val_R = func[:func.index(s_func)].count("R")
            numR.append(cnt)
        else:
            cnt += 1
    
    for num in numR:
        if num % 2 == 0 :
            try:
                nums.popleft()
            except:
                tick = 1
                print('error')
                break
        else:
            try:
                nums.pop()
            except:
                tick = 1
                print('error')
                break

    if tick:
        continue

    elif cnt % 2 == 0:
        for i in range(len(nums)):
            ans += str(nums[i]) + ","
        print('['+ans[:-1]+']')

    else:
        nums = list(nums)[::-1]
        for i in range(len(nums)):
            ans += str(nums[i]) + ","
        print('['+ans[:-1]+']')