from collections import deque
def checkPair(s):
    stack = []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(')')
        elif s[i] == '{':
            stack.append('}')
        elif s[i] == '[':
            stack.append(']')
        elif s[i] in ']})':
            if not stack or s[i] != stack[-1]:
                return 0
            stack.pop()
    return 0 if stack else 1

def solution(s):
    answer = 0
    s = deque(s)
    for i in range(len(s)):
        s.rotate(-1) #s.append(s.popleft())
        answer += checkPair(s)
        
    return answer
