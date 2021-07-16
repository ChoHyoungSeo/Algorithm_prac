x = []
y = []

for _ in range(3):
    a,b = map(int, input().split())
    
    if a not in x and b not in y:
        x.append(a)
        y.append(b)
    elif a in x and b in y:
        x.remove(a)
        y.remove(b)
    elif a not in x and b in y:
        x.append(a)
        y.remove(b)
    elif a in x and b not in y:
        x.remove(a)
        y.append(b)
        
print(x[0], y[0])