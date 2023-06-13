tot = int(input())
for _ in range(tot):
    change = int(input())
    ans = []
    a = change//25
    change %= 25
    b = change // 10
    change %= 10
    c = change//5
    change %= 5
    d = change
    
    ans.append(a)
    ans.append(b)
    ans.append(c)
    ans.append(d)
    print(' '.join(map(str,ans)))
    


##
n = int(input())

for _ in range(n):
	money = int(input())
	for i in [25, 10, 5, 1]:
		print(money//i, end=' ')
		money = money%i