cost = int(input())
change = 1000 - cost

a = change // 500 
change -= a * 500

b = change // 100
change -= b * 100

c = change // 50
change -= c * 50

d = change // 10
change -= d * 10

e = change // 5
change -= e * 5

f =  change // 1

print(a+b+c+d+e+f)

#-------------------------

cost = int(input())

change = 1000 - cost

a = change // 500 

b = (change - (500 * a)) // 100

c = (change - (500 * a) - (b * 100)) // 50

d = (change - (500 * a) - (b * 100) - (c * 50)) // 10

e = (change - (500 * a) - (b * 100) - (c * 50) - (d * 10)) // 5

f = (change - (500 * a) - (b * 100) - (c * 50) - (d * 10) - (e * 5)) // 1

print(a+b+c+d+e+f)