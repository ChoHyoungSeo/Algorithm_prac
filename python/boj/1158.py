# 드디어 다시 만난 요세푸스 문제,, 진짜 쉽네,,
# 1158
from collections import deque

tot, gap = map(int, input().split())
std = deque([x+1 for x in range(tot)])
ans = []

while True:
    if len(ans) == tot:
        break
    
    for i in range(gap-1):
        std.append(std.popleft())
    ans.append(std.popleft())

print("<", end = '')
print(', '.join(map(str, ans)), end = '')
print(">")