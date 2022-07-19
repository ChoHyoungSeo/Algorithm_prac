# 15829

_ = int(input())
words = list(map(str, input()))
i = 0
tmp = 0
ans = 0

for word in words:
    tmp = int(ord(word) - ord('a')+1) * (31 ** i)
    ans += tmp
    i += 1

print(ans % 1234567891)