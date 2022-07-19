word = input()
words = []

for i in range(len(word)):
    words.append(word[i:])

# words.sort(key = lambda x: x[0])
words.sort()
for i in range(len(words)):
    print(words[i])
# print(sorted(words, key = lambda x: x[0]), end="\n")