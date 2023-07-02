# 1. Union-find with hash (연결 여부 합집합) 재귀적
# 2. dict hash

def find(x):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[y] = x
        #network size
        number[x] += number[y]

test_case = int(input())

for _ in range(test_case):
    #use dict (input -> string)
    parent = dict()
    number = dict()

    f = int(input())

    for _ in range(f):
        x, y = input().split(' ')

        if x not in parent:
            parent[x] = x
            number[x] = 1
        
        if y not in parent:
            parent[y] = y
            number[y] = 1
        union(x, y)
        print(number[find(x)])