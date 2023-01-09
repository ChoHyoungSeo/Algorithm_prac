pool = set([x+1 for x in range(30)])
submit_group = set()

for _ in range(28):
  submit_group.add(int(input()))

print(sorted(list(pool - submit_group))[0])
print(sorted(list(pool - submit_group))[1])