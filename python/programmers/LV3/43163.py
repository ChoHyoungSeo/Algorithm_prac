from collections import deque

def can_transform(current, target):
    differences = 0
    for c, t in zip(current, target):
        if c != t:
            differences += 1
        if differences > 1:
            return False
    return True

def solution(begin, target, words):
    if target not in words:
        return 0

    queue = deque([(begin, 0)])
    visited = []

    while queue:
        current, steps = queue.popleft()
        if current == target:
            return steps

        for word in words:
            if word not in visited and can_transform(current, word):
                visited.append(word)
                queue.append((word, steps + 1))

    return 0