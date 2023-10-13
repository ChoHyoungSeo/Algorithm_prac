import sys
si = sys.stdin.readline
# 입력
n, m, k = map(int, si().split())
a = [list(map(int, si().split())) for _ in range(n)]
dirs = [[1, 0], [0, 1], [-1, 0], [0 ,-1]]

def in_range(x, y):  # 유효한 좌표인지 확인하는 함수
    return 0 <= x < n and 0 <= y < n

def detect_line(sx, sy):  # (sx, sy)가 머리사람일 때, 팀원들의 좌표 리스트를 머리부터 꼬리까지 "순서대로" 돌려주는 함수
    teammates = [(sx, sy)]
    # 머리에서 시작해서 한 칸씩 꼬리를 향하여 이동하자!
    x, y = sx, sy
    while a[x][y] != 3:
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if not in_range(nx, ny): continue  # 격자를 벗어나지 않고
            if len(teammates) >= 2 and (nx, ny) == teammates[-2]: continue  # 머리 쪽으로 다시 돌아가지 않고
            if a[x][y] == 1 and a[nx][ny] == 3: continue  # 머리인 경우에는 꼬리로 가지 않고
            if a[nx][ny] not in [2, 3]: continue  # 이동선 위를 벗어나지 않는다면 (4는 말고 2나 3으로만 가야지)
            x, y = nx, ny  # 성공적으로 꼬리 쪽 방향임을 알 수 있다.
            break
        teammates.append((x, y))
    return teammates

def detect_whole_teams():  # 모든 팀의 좌표를 찾아주는 함수
    teams = []
    # 1. 모든 머리를 찾고
    for i in range(n):
        for j in range(n):
            if a[i][j] == 1:
                # 2. 각 팀을 찾는 함수
                teams.append(detect_line(i, j))
    return teams

def move_one_team(teammates):  # teammates 가 한 팀을 순서대로 쓴 경우
    # 머리가 이동할 좌표 찾기
    x, y = teammates[0] #머리 좌표
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy #인접한 위치 중에서 4의 위치를 찾기
        if not in_range(nx, ny): continue
        if a[nx][ny] not in [3, 4]: continue
        break
    # 인접한 좌표 중 3 혹은 4가 써있는 위치를 찾았다.
    # nx, ny := 머리가 이동할 위치
    new_coords = []  # 각 팀원이 가게 될 좌표
    for teammate in teammates: #teammates의 머리부터 꼬리까지 보면서 
        cx, cy = teammate  # (cx, cy) := 지금 보고 있는 위치
        new_coords.append((nx, ny))
        nx, ny = cx, cy
        a[cx][cy] = 4
        # 4 1 2 3 있을 때 -> 1 4 2 3 -> 1 2 4 3 -> 1 2 3 4

    for idx, (x, y) in enumerate(new_coords):
        if idx == 0:  # 머리가 새롭게 이동한 위치
            a[x][y] = 1
        elif idx == len(new_coords) - 1:  # 꼬리가 새롭게 이동한 위치
            a[x][y] = 3
        else:  # 몸이 새롭게 이동한 위치
            a[x][y] = 2

def move_whole_teams():
    # 1. 모든 팀을 찾고
    teams = detect_whole_teams()
    # 2. 한 칸씩 이동시켜주는 함수
    for teammates in teams:
        move_one_team(teammates)

def throw_ball(round_num):
    # 공을 조건에 맞게 던지고, 충돌하는 좌표를 돌려주기
    round_num %= n * 4
    if round_num < n:
        x1, y1 = round_num, 0 #시작
        x2, y2 = round_num, n #끝
    elif round_num < n * 2:
        x1, y1 = n - 1, round_num - n
        x2, y2 =    -1, round_num - n
    elif round_num < n * 3:
        x1, y1 = (3 * n - 1) - round_num, n - 1
        x2, y2 = (3 * n - 1) - round_num, -1
    else:
        x1, y1 = 0, (4 * n - 1) - round_num
        x2, y2 = n, (4 * n - 1) - round_num
    
    # (x1, y1)에서 시작해서 (x2, y2) 방향으로 공을 던질 것이다.
    dx, dy = (x2 - x1) // n, (y2 - y1) // n
    x, y = x1, y1
    while (x, y) != (x2, y2): #공이 움직인다.
        if a[x][y] not in [0, 4]: #어딘가 충돌했다.
            return (x, y)
        x, y = x + dx, y + dy
    return None

def calculate(coord):  # 팀 반전 및 점수 계산
    teams = detect_whole_teams()
    for teammates in teams:
        for idx, teammate in enumerate(teammates, 1):
            if teammate == coord:
                # 머리와 꼬리를 바꿔주는 작업
                x1, y1 = teammates[0]
                x2, y2 = teammates[-1]
                a[x1][y1], a[x2][y2] = a[x2][y2], a[x1][y1]
                return idx * idx  # 공을 받은 사람은 idx 번째 위치에 서있음

ans = 0 
for round_num in range(k):
    move_whole_teams()                # 각 팀을 한 칸 이동시키기
    coord = throw_ball(round_num)     # 공 던지기
    if coord is None:
        continue
    ans += calculate(coord)           # 팀 반전 및 점수 계산
print(ans)