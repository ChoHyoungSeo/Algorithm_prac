v, f, cost = map(int, input().split())

if cost - f <= 0:
    print("-1")
    
else:
    print(int((v/(cost-f))+1))
