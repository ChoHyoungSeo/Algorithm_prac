#1259
while True:
    num = str(input())
    if num == "0":
        break
    
    elif num[::-1] == num:
        print("yes")
    else:
        print("no")