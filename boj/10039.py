#10039
scores = []
ans = 0

for _ in range(5):
    scores.append(int(input()))

for score in scores:
    if score < 40:
        score = 40
    ans += score

print(int(ans/5))