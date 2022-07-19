#데크가 나을것 같은데 인덱스를 이용하면서 하나씩 보는 방법도 업데이트

from collections import deque
 
tot, gap = map(int, input().split())
deq = deque(x+1 for x in range(tot))

print("<",end='')
while deq:
    for _ in range(gap-1):
        deq.append(deq.popleft())
    print(deq.popleft(), end="")    
    if deq:
        print(", ", end="")
    else:
        continue
print(">")