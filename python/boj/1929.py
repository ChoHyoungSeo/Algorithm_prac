import sys
a,b = map(int, sys.stdin.readline().split())

for i in range(a, b+1):
    if i == 1:
        continue
    else:
        cnt = 0
        for j in range(2, int((i**0.5))+1): #tip,, use square root
            if i % j == 0:
                cnt = 1
                break
        if cnt == 0:
            print(i)

# should improve time complexity