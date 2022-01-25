#2525
hour, minute = map(int, input().split())
dur = int(input())

hour += (minute + dur) // 60
minute = (minute + dur) % 60

if hour > 23:
    hour -= 24

print(hour, minute)