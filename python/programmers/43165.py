# dfs
def dfs(numbers, target, index, total):
    if index == len(numbers):
        return 1 if total == target else 0
    return dfs(numbers, target, index + 1, total + numbers[index]) + dfs(numbers, target, index + 1, total - numbers[index])

def solution(numbers, target):
    return dfs(numbers, target, 0, 0)

# bfs
from collections import deque

def solution(numbers, target):
    queue = deque()
    queue.append((0, 0))  # 시작점 (합계, 인덱스)

    count = 0
    while queue:
        total, index = queue.popleft()

        if index == len(numbers):
            if total == target:
                count += 1
        else:
            queue.append((total + numbers[index], index + 1))
            queue.append((total - numbers[index], index + 1))

    return count