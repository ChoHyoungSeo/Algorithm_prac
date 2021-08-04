a  = int(input())
for i in range(a):
    if ((3*(i**2) + (3*i) + 1) >= a):
        ans = i
        break
print(ans+1)

#Use sequence