tot = int(input())

for i in range(tot):
    n, s = input().split()

    for x in s:
        print(x*int(n), end='')
        
    print()