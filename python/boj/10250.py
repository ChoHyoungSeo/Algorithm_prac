a = int(input())

for i in range(a):
    height, width, number = map(int, input().split())
    floor = number % height

    if floor == 0:
        floor = height
        n = (number // height)

    elif floor != 0:
        n = (number // height) + 1

    if n < 10:        
        print(str(floor)+ "0" + str(n))
    
    else:
        print(str(floor)+str(n))