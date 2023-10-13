a, b = map(int, input().split())
pool = []
tmp = a

while True:
    tmp = (tmp * a) % b
    if tmp in pool:
        print(len(pool) - pool.index(tmp))
        break
    pool.append(tmp)
