#print(chr(97)) #a
#print(chr(122)) # z
cnt = 0
alp = [x for x in range(97,123)]
ans = [0 for _ in range(97,123)]
a = list(input().lower())

for i in range(len(a)):
    k = alp.index(ord(a[i]))
    ans[k] += 1

for i in range(len(ans)):
    if max(ans) == ans[i]:
        cnt += 1
    else:
        continue
        
if cnt > 1:
    print("?")
else:
    ans_idx = ans.index(max(ans))
    print(chr(alp[ans_idx]).upper())