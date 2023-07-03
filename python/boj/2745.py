N, B = input().split(" ")
N = ''.join(reversed(N))
B = int(B)

number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = 0

for x in range(len(N)-1, -1, -1):
    result += number.index(N[x]) * (B**x)
print(result)

n, b = input().split()
print(int(n, int(b)))