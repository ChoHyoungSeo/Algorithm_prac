def diffuse(graph):
    r, c = len(graph), len(graph[0])
    temp_graph = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if graph[i][j] > 0:
                spread_amount = graph[i][j] // 5
                spread_count = 0
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != -1:
                        temp_graph[nx][ny] += spread_amount
                        spread_count += 1
                graph[i][j] -= spread_amount * spread_count
    for i in range(r):
        for j in range(c):
            graph[i][j] += temp_graph[i][j]

def clean_air(graph, air_condition):
    r, c = len(graph), len(graph[0])
    up, down = air_condition[0], air_condition[0] + 1

    # Top part counter-clockwise
    for i in range(up-1, 0, -1):  # Down to top
        graph[i][0] = graph[i-1][0]
    for j in range(0, c-1):  # Left to right
        graph[0][j] = graph[0][j+1]
    for i in range(0, up):  # Top to down
        graph[i][c-1] = graph[i+1][c-1]
    for j in range(c-1, 1, -1):  # Right to left
        graph[up][j] = graph[up][j-1]
    graph[up][1] = 0  # Clean air

    # Bottom part clockwise
    for i in range(down+1, r-1):  # Top to down
        graph[i][0] = graph[i+1][0]
    for j in range(0, c-1):  # Left to right
        graph[r-1][j] = graph[r-1][j+1]
    for i in range(r-1, down, -1):  # Down to top
        graph[i][c-1] = graph[i-1][c-1]
    for j in range(c-1, 1, -1):  # Right to left
        graph[down][j] = graph[down][j-1]
    graph[down][1] = 0  # Clean air

if __name__ == '__main__':
    r, c, t = list(map(int, input().split()))
    graph = [list(map(int, input().split())) for _ in range(r)]
    air_condition = (0, 0)

    for i in range(r):
        if graph[i][0] == -1:
            air_condition = (i, 0)
            break

    for _ in range(t):
        diffuse(graph)
        clean_air(graph, air_condition)

    print(sum(sum(cell for cell in row if cell > -1) for row in graph))
