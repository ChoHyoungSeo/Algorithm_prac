#can improve
alp = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
in_alp = str(input())
cnt = 0
word_dict = {}
tmp = 0

for word in alp:
    word_dict[word] = in_alp.count(word)
word_dict["z="] -= word_dict["dz="]
for key, val in word_dict.items():
    tmp += len(key) * val
    cnt += val

cnt += len(in_alp) - tmp
print(cnt)
