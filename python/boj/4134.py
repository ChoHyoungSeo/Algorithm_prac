import sys
import math
input=sys.stdin.readline
tot=int(input())

def check(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            return False
    return True

for i in range(tot):
    target=int(input())
    while True:
        if target==0 or target==1:
            print(2)
            break
        if check(target):
            print(target)
            break
        else:
            target+=1