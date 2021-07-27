# timeover error

# up, down, tot = map(int,input().split())
# cnt = 0
# ans = 0
# while(True):
#     if cnt >= tot:
#         print(ans)
#         break
#     elif cnt + up >= tot:
#         print(ans + 1)
#         break
#     else:
#         ans += 1
#         cnt += (up - down)

#new_answer

up, down, tot = map(int,input().split())
res = tot - up
dif = up - down
if res <= 0:
    print(1)
else:
    if res % dif != 0:
        print((res // dif) + 2)
    else:
        print((res//dif) + 1)