
import sys

tot, ques = map(int, sys.stdin.readline().strip().split())
names = []
poke_dict = dict()

for i in range(tot):
    tmp = sys.stdin.readline().strip()
    names.append(tmp)
    poke_dict[tmp] = i

for i in range(ques):
    temp = sys.stdin.readline().strip()
    if temp.isdigit():
        print(names[int(temp)-1])
    else:
        print(poke_dict[temp]+1)