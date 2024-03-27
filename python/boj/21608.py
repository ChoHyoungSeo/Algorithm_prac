# # 좋아하는 학생이 인접한 칸에 많은 자리
# # 인접한 칸 중에서 남은 칸이 가장 많은 자리
# # 행의 번호가 가장 작은 칸, 열의 번호가 가장 작은 칸


# # 자리 배치 끝나면 만족도 구하기
# # 만족도는 인접한 칸에 앉은 좋아하는 학생의 수에 따라 다르다
# # 0명: 0, 1명: 1, 2명: 10, 3명: 100, 4명: 1000

# # 만족도 총합

# n = int(input())
# students = []
# graph = [[0] * n for _ in range(n)]

# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]

# for _ in range(n*n):
#     students.append(list(map(int, input().split())))

# for student in students:
#     possible_seat = []
#     for i in range(n):
#         for j in range(n):
#             if graph[i][j] == 0:
#                 like, empty = 0, 0
#                 for k in range(4):
#                     nx, ny = i + dx[k], j + dy[k]
#                     if 0 <= nx < n and 0 <= ny < n:
#                         if graph[nx][ny] in student[1:]:
#                             like += 1
#                         elif graph[nx][ny] == 0:
#                             empty += 1
#                 possible_seat.append((like, empty, i, j))
#     possible_seat.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
#     graph[possible_seat[0][2]][possible_seat[0][3]] = student[0]

# answer = 0
# students.sort()

# for i in range(n):
#     for j in range(n):
#         score = 0
#         for k in range(4):
#             nx, ny = i + dx[k], j + dy[k]
#             if 0 <= nx < n and 0 <= ny < n:
#                 if graph[nx][ny] in students[graph[i][j] - 1]:
#                     score += 1
#         if score != 0:
#             answer += 10 ** (score - 1)
# print(answer)

import sys
from collections import defaultdict
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
n = int(input())
seats = [[0] * n for _ in range(n)]
students_preferences = {}
answer = 0

for _ in range(n ** 2):
    student = list(map(int, input().split()))
    students_preferences[student[0]] = set(student[1:])

for student, preferences in students_preferences.items():
    possible = []
    for x in range(n):
        for y in range(n):
            if not seats[x][y]:
                empty = 0
                friend = 0
                for direction in range(4):
                    nx = dx[direction] + x
                    ny = dy[direction] + y
                    if 0 <= nx < n and 0 <= ny < n:
                        if not seats[nx][ny]:
                            empty += 1
                        elif seats[nx][ny] in preferences:
                            friend += 1
                possible.append((friend, empty, x, y))
    possible.sort(key=lambda k: (-k[0], -k[1], k[2], k[3]))
    _, _, best_x, best_y = possible[0]
    seats[best_x][best_y] = student

for x in range(n):
    for y in range(n):
        me = seats[x][y]
        friend_count = 0
        for direction in range(4):
            nx = dx[direction] + x
            ny = dy[direction] + y
            if 0 <= nx < n and 0 <= ny < n and seats[nx][ny] in students_preferences[me]:
                friend_count += 1
        if friend_count:
            answer += 10 ** (friend_count - 1)

print(answer)
