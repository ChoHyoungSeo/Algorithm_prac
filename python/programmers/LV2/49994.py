def check(x, y):
    if 0 <= x < 11 and 0 <= y < 11:
        return True
    return False

def solution(dirs):
    x, y =5, 5
    path = set()
    
    for dir in dirs:
        nx, ny = x, y
        if dir =='U':
            nx -= 1
        elif dir == 'D':
            nx += 1
        elif dir == 'R':
            ny += 1
        elif dir == 'L':
            ny -= 1
        
        if check(nx, ny):
            path.add((x, y, nx, ny))
            path.add((nx, ny, x, y))
            x, y = nx, ny

    return len(path)//2