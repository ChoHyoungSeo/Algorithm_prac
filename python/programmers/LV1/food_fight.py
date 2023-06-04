def solution(food):
    answer = ''
    for i in range(1,len(food)):
        if food[i] // 2:
            answer += str(i) * int(food[i] // 2)
    rev_answer = answer[::-1]
    answer += '0'
    answer += rev_answer
    return answer