import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    stack = []
    valid = True
    for paren in input().strip():
        if paren == '(':
            stack.append('(')
        elif stack:
            stack.pop()
        else:
            valid = False
            break
    print("YES" if valid and not stack else "NO")
