#only 75
#should avoid time error
def solution(number, k):
    answer = ''
    tmp_number = number

    if len(number) - k == k:
        tmp_k = k
        
    else:
        tmp_k = len(number) - k - 1
    
    if len(number) - k == 1:
        return max(int(number))
    
    while True:
        if len(answer) == len(number) - k:
            break
        elif tmp_k == 1:
            if len(number) - k <= len(tmp_number):
                answer += max(tmp_number)
                break
            else:
                answer += tmp_number
                break
        try:
            max_num = max(tmp_number[:-tmp_k])
            answer += max_num
            loc = tmp_number.find(max_num)
            tmp_number = tmp_number[loc+1:]
            tmp_k -= 1
            
        except:
            break
        
    return answer