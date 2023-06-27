# a = int(input())

# for i in range(a):
#     score = list(map(int, input().split()))
#     rscore = score[1:]
#     avg = sum(rscore)/len(rscore)
#     cnt = 0
    
#     for j in range(len(rscore)):
#         if rscore[j] > avg :
#             cnt += 1
        
#         else:
#             continue

#     print(str("%.3f" %((cnt/len(rscore)) * 100)) + "%")

n = int(input())

for _ in range(n):
    nums = list(map(int, input().split()))
    avg = sum(nums[1:])/nums[0]
    cnt = 0
    for score in nums[1:]:
        if score > avg:
            cnt += 1
    rate = cnt/nums[0] *100
    print(f'{rate:.3f}%')