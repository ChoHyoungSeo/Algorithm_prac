from collections import deque
import sys

input = sys.stdin.readline
gears = [deque(list(map(int, input().rstrip()))) for _ in range(4)]
a = int(input())
comm = [list(map(int, input().split())) for _ in range(a)]

def rotate(idx, dir, gears):
    if dir == -1:
        gears[idx].append(gears[idx].popleft())
    elif dir == 1:
        gears[idx].appendleft(gears[idx].pop())

def check_and_rotate(idx, dir, gears):
    dirs = [0] * 4  # 각 톱니바퀴의 회전 방향을 저장
    dirs[idx] = dir

    # 왼쪽 톱니바퀴 체크
    for i in range(idx, 0, -1):
        if gears[i][6] != gears[i-1][2]:
            dirs[i-1] = -dirs[i]
        else:
            break

    # 오른쪽 톱니바퀴 체크
    for i in range(idx, 3):
        if gears[i][2] != gears[i+1][6]:
            dirs[i+1] = -dirs[i]
        else:
            break

    # 톱니바퀴 회전
    for i in range(4):
        if dirs[i]:
            rotate(i, dirs[i], gears)

for com in comm:
    check_and_rotate(com[0]-1, com[1], gears)

answer = 0
for i in range(4):
    if gears[i][0] == 1:
        answer += 2**i
print(answer)
