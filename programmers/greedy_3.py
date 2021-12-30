def solution(number, k):
    answer = ''
    
    for num in number:
        while answer and k > 0 and answer[-1] < num:
            answer = answer[:-1]
            k -= 1
        answer += num
    
    # list를 str 으로 바꿔줄 때 이 부분을 놓쳤다
    # testcase 12번은 이 부분을 넣어줘야 맞추는 문제구나
    if k != 0:
        answer = answer[:-k]
        
    return answer