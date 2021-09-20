a = int(input())

for _ in range(a):
    tot, target = list(map(int, input().split()))
    imp = list(map(int, input().split()))
    idx = list(range(len(imp)))
    idx[target] = 'target'
    loc = 0
    while True:
        if imp[0] == max(imp):
            loc += 1       
            if idx[0] == 'target':
                print(loc)
                break
            else:
                imp.pop(0)
                idx.pop(0)
        else:
            imp.append(imp.pop(0))
            idx.append(idx.pop(0))