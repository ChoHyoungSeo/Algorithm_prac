from collections import deque
while True:
    ans = ''
    a = int(input())
    if a == -1:
        break
    tmp = []
    for i in range(1, a):
        if a % i == 0:
            tmp.append(i)
    tmp = deque(tmp)
    if sum(tmp) == a:
        while tmp:
            num = tmp.popleft()
            if tmp:
                ans += str(num) + ' + '
            else:
                ans += str(num)
        print(a,"=",ans)
    else:
        print("%d is NOT perfect." %a)