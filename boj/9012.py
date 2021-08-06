a = int(input())
ibraket = []

for _ in range(a):
    ibraket = list(input())
    ans = []
    for b in ibraket:
        if b == "(":
            ans.append("(")
        else:
            try:
                ans.remove(ans[-1])
            except:
                ans = True
                break
    if ans:
        print("NO")
        
    else:
        print("YES")