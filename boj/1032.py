a = int(input())
words = []
ans = ''
for i in range(a):
    words.append(input())

for i in range(len(words[0])):
    std = words[0][i]
    tick = False
    for word in words:
        if word[i] != std:
            ans += "?"
        tick = True
        break
    if not tick:
      ans += std

print(ans)
