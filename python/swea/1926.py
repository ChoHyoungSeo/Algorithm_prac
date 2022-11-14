1926 
tot = int(input())
num_list = [str(x) for x in range(1, tot+1)]
ans = []
for num in num_list:
  if "3" in num or "6" in num or "9" in num:
    a, b, c=num.count("3"), num.count("6"), num.count("9")
    num = num.replace(num, "-"*(a+b+c))
    ans.append(num)
  else:
    ans.append(num)
print(*ans)