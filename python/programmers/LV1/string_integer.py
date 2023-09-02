def solution(s):
    answer = []
    tmp = ''
    num_dict = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    for i in range(len(s)):
        if s[i].isdigit():
            answer.append(s[i])
        else:
            tmp += s[i]
        if tmp in num_dict.keys():
            answer.append(num_dict[tmp])
            tmp = ''
    
    return int(''.join(answer))