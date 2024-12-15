from collections import deque

def bfs(num1, num2):
    queue = deque()
    step = 0
    queue.append((num1, step))

    while queue:
        current, step = queue.popleft()
        if current == num2:
            return step + 1
        
        if current * 2 <= num2:
            queue.append((current*2, step+1))
        if current * 10 + 1 <= num2:
            queue.append((current*10+1, step+1))
    return -1

if __name__ =='__main__':
    start, end = map(int, input().split())
    print(bfs(start, end))