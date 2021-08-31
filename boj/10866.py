from collections import deque
import sys
a = int(sys.stdin.readline().strip())
ans_deq = deque()
for i in range(a):
    com = sys.stdin.readline().strip().split()
    if com[0] == 'push_front':
        ans_deq.appendleft(com[1])
    elif com[0] == 'push_back':
        ans_deq.append(com[1])
    elif com[0] == 'pop_front':
        if ans_deq:
            print(ans_deq.popleft())
        else:
            print(-1)
    elif com[0] == 'pop_back':
        if ans_deq:
            print(ans_deq.pop())
        else:
            print(-1)
    elif com[0] == 'size':
        print(len(ans_deq))
    elif com[0] == 'empty':
        if ans_deq:
            print(0)
        else:
            print(1)
    elif com[0] == 'front':
        if ans_deq:
            print(ans_deq[0])
        else:
            print(-1)
    elif com[0] == 'back':
        if ans_deq:
            print(ans_deq[-1])
        else:
            print(-1)