# 1620
# import sys

# tot, ques = map(int, sys.stdin.readline().strip().split())
# poke_dict = dict()
# reversed_dict = dict()

# for i in range(1, tot+1):
#     poke_dict[i] = str(sys.stdin.readline().strip())
   
# reversed_dict= dict(map(reversed, poke_dict.items()))
# for i in range(ques):
#     ans = input()

#     try:
#         if int(ans) in poke_dict:
#             print(poke_dict[int(ans)])    
#     except:
#         print(reversed_dict[ans])

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