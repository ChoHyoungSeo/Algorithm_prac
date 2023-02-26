tot, shot  = map(int, input().split())
basket_dict = {k: k for k in range(1, tot+1)}

for _ in range(shot):
  a, b = map(int, input().split())
  basket_dict[a], basket_dict[b] = basket_dict[b], basket_dict[a]

for vals in basket_dict.values():
  print(vals, end=' ')