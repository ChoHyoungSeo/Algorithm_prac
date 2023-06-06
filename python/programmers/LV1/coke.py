def solution(a, b, n):
    answer = 0
    
    while True:
        new_coke = n // a * b
        rest_coke = n % a
        n = new_coke+rest_coke
        answer += new_coke
        if n < a:
            break
    return answer