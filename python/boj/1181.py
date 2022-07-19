a = int(input())
words = []

for i in range(a):
    word = input()
    words.append((word, len(word)))
words = list(set(words))
words.sort(key = lambda x : (x[1], x[0]))

for i in range(len(words)):
    print(words[i][0])