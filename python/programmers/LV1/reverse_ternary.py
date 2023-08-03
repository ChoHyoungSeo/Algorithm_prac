def solution(n):
    tmp = []
    while n != 0:
        tmp.append(str(n%3))
        n //= 3
    target = ''.join(tmp)
    return int(target,3)