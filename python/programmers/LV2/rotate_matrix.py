# def rotate(x1, y1, x2, y2, matrix):
#     first = matrix[x1][y1]
#     min_value = first
    
#     #왼쪽
#     for k in range(x1, x2):
#         matrix[k][y1] = matrix[k+1][y1]
#         min_value = min(min_value, matrix[k+1][y1])
        
#     #아래
#     for k in range(y1, y2):
#         matrix[x2][k] = matrix[x2][k+1]
#         min_value = min(min_value, matrix[x2][k+1])
    
#     #오른쪽
#     for k in range(x2, x1, -1):
#         matrix[k][y2] = matrix[k-1][y2]
#         min_value = min(min_value, matrix[k-1][y2])
#     #위
#     for k in range(y2, y1+1, -1):
#         matrix[x1][k] = matrix[x1][k-1]
#         min_value = min(min_value, matrix[x1][k-1])
    
#     matrix[x1][y1+1] = first
#     return min_value

# def solution(rows, columns, queries):
#     matrix = [[(i) * columns + (j+1) for j in range(columns)] for i in range(rows)]
#     result = []
#     for x1, y1, x2, y2 in queries:
#         result.append(rotate(x1-1, y1-1, x2-1, y2-1, matrix))
#     return result

def solution(rows, columns, queries):
    answer = []
    board = [[columns * j + (i+1) for i in range(columns)] for j in range(rows)]
    for query in queries:
        a, b, c, d = query[0] - 1, query[1] - 1, query[2] - 1, query[3] - 1
        row1, row2 = board[a][b:d], board[c][b+1:d+1]
        _min = min(row1+row2)
        
        for i in range(c, a, -1):
            board[i][d] = board[i-1][d]
            if board[i][d] < _min: _min = board[i][d]

        for i in range(a, c):
            board[i][b] = board[i+1][b]
            if board[i][b] < _min: _min=board[i][b]

        board[a][b+1:d+1], board[c][b:d] = row1, row2

        answer.append(_min)

    return answer