a = int(input())
b = int(input())
tmp = []
c = str(b)

for i in range(len(c)):
    tmp.append(c[i])
    
for i in range(len(c)-1, -1, -1):
    print(a*int(tmp[i]))
    
print(a*b)