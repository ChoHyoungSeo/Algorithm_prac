from collections import deque
import sys
input = sys.stdin.readline

num = int(input().strip())
cards = deque([i+1 for i in range(num)])

while len(cards) != 1:
    cards.popleft()
    cards.append(cards.popleft())
print(*cards)