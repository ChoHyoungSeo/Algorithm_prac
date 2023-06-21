def solution(x):
    std = 0
    for i in range(len(str(x))):
        std += int(str(x)[i])
    if x % std == 0 :
        return True
    return False