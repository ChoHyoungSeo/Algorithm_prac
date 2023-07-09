def solution(s):
    answer = s.isdigit()
    if answer:
        if len(s) == 4 or len(s) == 6:
            return True
        else:
            return False
    return False