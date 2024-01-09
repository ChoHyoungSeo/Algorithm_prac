from collections import deque
cx = [0, 0, 1, -1]
cy = [1, -1, 0, 0]
def bfs(a, b, visited, land, n, m):
    if land[a][b] == 0:
        return 0

    count = 0
    min_col, max_col = m, 0
    queue = deque()
    queue.append((a, b))
    visited[a][b] = True

    while queue:
        x, y = queue.popleft()
        min_col = min(min_col, y)
        max_col = max(max_col, y)
        count += 1
        for dx, dy in zip(cx, cy):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and land[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True

    return count, min_col, max_col

def solution(land):
    n = len(land)
    m = len(land[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    oil_per_column = [0 for _ in range(m)]

    for row in range(n):
        for col in range(m):
            if not visited[row][col] and land[row][col]:
                oil, min_col, max_col = bfs(row, col, visited, land, n, m)
                for c in range(min_col, max_col + 1):
                    oil_per_column[c] += oil

    return max(oil_per_column)

# 시간초과
# from collections import deque

# cx = [0, 0, 1, -1]
# cy = [1, -1, 0, 0]

# def bfs(a, b, visited, land, n, m):
#     if land[a][b] == 0:
#         return 0

#     count = 0
#     queue = deque()
#     queue.append((a, b))
#     visited[a][b] = True

#     while queue:
#         x, y = queue.popleft()
#         count += 1
#         for dx, dy in zip(cx, cy):
#             nx, ny = x + dx, y + dy
#             if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and land[nx][ny]:
#                 queue.append((nx, ny))
#                 visited[nx][ny] = True

#     return count

# def solution(land):
#     n = len(land)
#     m = len(land[0])
#     max_oil = 0

#     for col in range(m):
#         visited = [[False for _ in range(m)] for _ in range(n)]
#         oil = 0
#         for row in range(n):
#             if not visited[row][col] and land[row][col]:
#                 oil += bfs(row, col, visited, land, n, m)
#         max_oil = max(max_oil, oil)

#     return max_oil