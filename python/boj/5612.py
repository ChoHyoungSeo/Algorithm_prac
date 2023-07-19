tot = int(input())
start = int(input())
current = start
candid = [start]
flag = False
for _ in range(tot):
    in_car, out_car = map(int, input().split())
    current += in_car
    current -= out_car
    if current < 0 :
        flag = True
        print(0)
        break
    candid.append(current)
if not flag:
    print(max(candid))