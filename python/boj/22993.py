#22993
from collections import deque

tot = int(input())
attack = deque(map(int, input().split()))
std = attack.popleft()
attack = deque(sorted(list(attack)))

while attack:
    if attack[0] >= std:
        ans = "No"
        break
    std += attack[0]
    attack.popleft()

if not attack:
    ans = "Yes"

print(ans)