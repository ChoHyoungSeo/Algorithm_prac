def solution(s):
    words = list(map(str, s))
    stack = []
    for word in words:
        if not stack:
            stack.append(word)
        elif stack[-1] == word:
            stack.pop()
        else:
            stack.append(word)
    if stack:
        return 0
    else:
        return 1