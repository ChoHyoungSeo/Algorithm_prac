#10808
words = list(map(str,input()))
alp = [0] * 26

for word in words:
    alp[ord(word) - ord('a')] += 1

for i in range(len(alp)):
    print(alp[i], end=' ')