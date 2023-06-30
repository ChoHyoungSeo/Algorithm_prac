# def solution(n):
#     answer = []
#     dx = [0, 1, -1]
#     dy = [1, 0, -1]
#     snail = [[0] * i for i in range(1, n+1)]
#     x = y = angle = 0
#     cnt = 1
#     size = (n+1) * n // 2 #len(snail) 과 같다
    
#     while cnt <= size:
#         snail[y][x] = cnt
#         ny = y + dy[angle]
#         nx = x + dx[angle]
#         cnt += 1
        
#         if 0 <= ny < n and 0 <= nx <= ny and snail[ny][nx] == 0:
#             y, x = ny, nx
#         else:
#             angle = (angle + 1) % 3
#             y += dy[angle]
#             x += dx[angle]
#     return [i for j in snail for i in j]


#optimize
def solution(n):
    res = [[0] * i for i in range(1, n+1)]
    y, x = -1, 0
    num = 1
    
    for i in range(n):
        for _ in range(i, n):
            angle = i % 3
            # 아래 -> 오른쪽 -> 대각선위
            if angle == 0: y += 1
            elif angle == 1: x += 1   
            elif angle == 2: y -= 1; x -= 1      
            res[y][x] = num
            num += 1
    # flatten 
    return [i for j in res for i in j]