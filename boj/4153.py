while True:
    length = []
    a,b,c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    
    length.append(a)
    length.append(b)
    length.append(c)
    length.sort()

    if length[0]*length[0] + length[1]*length[1] == length[2]*length[2]:
        print("right")
    else:
        print("wrong")