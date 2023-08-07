score1, score2, score3 = map(int, input().split())
tot = int(input())
candid = []
for _ in range(tot):
    team = []
    for _ in range(3):
        tmp1, tmp2, tmp3 = map(int, input().split())
        team.append(tmp1*score1 + tmp2*score2 + tmp3*score3)
    candid.append(sum(team))
print(max(candid))