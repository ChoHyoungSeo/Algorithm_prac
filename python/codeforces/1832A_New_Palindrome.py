from collections import Counter
tot = int(input())
for _ in range(tot):
    target = list(input())
    string_dict = Counter(target)
    values_list = sorted(string_dict.values())
    if len(set(target)) >= 2 and values_list[-1] >= 2 and values_list[-2] >= 2:
        print("Yes")
    else:
        print("No")