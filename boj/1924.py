cnt = 0
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
mon,day = map(int,input().split())

for i in range(mon - 1):
    cnt = cnt + days[i]
cnt = (cnt + day) % 7

print(days[cnt])