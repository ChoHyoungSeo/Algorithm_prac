#17219
tot, inp = map(int, input().split())
ID_dict = {}

for _ in range(tot):
    id, pw = map(str, input().split())
    ID_dict[id] = pw

for _ in range(inp):
    print(ID_dict[input()])