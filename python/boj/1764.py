#1764
# time error
# hear, see = map(int, input().split())
# hear_list = []
# see_list = []
# both_list = []

# for _ in range(hear):
#     hear_list.append(input())

# for _ in range(see):
#     see_list.append(input())

# for name in hear_list:
#     if name in see_list:
#         both_list.append(name)

# print(len(both_list))
# for i in range(len(both_list)):
#     print(both_list[i])



import sys
hear, see = map(int, sys.stdin.readline().strip().split())
hear_set = set()
see_set = set()
both_set = set()

for _ in range(hear):
    hear_set.add(sys.stdin.readline().strip())
   
for _ in range(see):
    see_set.add(sys.stdin.readline().strip())

both_set = hear_set & see_set

print(len(both_set))
for name in sorted(list(both_set)):
    print(name)