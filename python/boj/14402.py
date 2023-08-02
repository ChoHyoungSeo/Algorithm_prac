tot = int(input())
work = []
cnt = 0
for _ in range(tot):
    name, target = map(str, input().split())
    if target == '+':  
        work.append(name)
    elif target == '-':
        if name not in work:
            cnt += 1
        else:
            work.remove(name)
if work:
    cnt += len(work)
print(cnt)
            