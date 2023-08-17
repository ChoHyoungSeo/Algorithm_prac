from collections import deque

tot = int(input())
pool = set()

for _ in range(tot):
    words = deque(map(str, input()))
    flag = False
    for i in range(len(words)):
        words.append(words.popleft())
        tmp = ''.join(words)
        if tmp in pool:
            flag = True
            break
    if not flag:
        pool.add(''.join(words))
print(len(pool))