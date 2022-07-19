#new_answer
a = int(input())
b = int(input())
ans = []

for i in range(a,b+1):
    cnt = 0
    for j in range(1,i):
        if i % j == 0:
            cnt += 1
            if cnt > 1: #for short time
                break
        else:
            continue
    if cnt == 1:
        ans.append(i)

if len(ans) == 0:
    print("-1")
else:
    print(sum(ans))
    print(min(ans))


# timeover error

# a = int(input())
# b = int(input())
# ans = []

# for i in range(a,b+1):
#     cnt = 0
#     for j in range(1,i):
#         if i % j != 0:
#             continue
#         elif i % j == 0:
#             cnt += 1
#     if cnt == 1:
#         ans.append(i)

# if len(ans) == 0:
#     print("-1")
# else:
#     print(sum(ans))
#     print(min(ans))