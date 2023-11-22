def solution(a, b):
    answer = ['THU','FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    day = 0
    for i in range(1, a):
        if i in [1,3,5,7,8,10,12]:
            day += 31
        elif i in [4,6,9,11]:
            day += 30
        elif i == 2:
            day += 29
    day += b
    return answer[day%7]