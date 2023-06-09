tot = int(input())
cars_dict = dict()
ans = 0
for i in range(1, tot+1):
	speed, durability = map(int, input().split())
	if speed in cars_dict.keys():
		if cars_dict[speed][0] <= durability:
			cars_dict[speed][0] = durability
			cars_dict[speed][-1] = i
	else:
		cars_dict[speed] = [durability, i]
	
for k, v in cars_dict.items():
	ans += v[-1]
print(ans)