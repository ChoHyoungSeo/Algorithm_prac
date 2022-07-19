ans = []
a = int(input())

for i in range(a):
    inp = int(input())
    if inp == 0:
        del ans[-1]
    else:
        ans.append(inp)

print(sum(ans))