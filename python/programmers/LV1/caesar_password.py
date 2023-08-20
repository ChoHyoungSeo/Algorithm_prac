# # 97
# # 122
# # 65
# # 90

# def solution(s, n):
#     answer = ''
#     words = list(map(str, s.split()))
#     for word in words:
#         for i in range(len(word)):
#             flag = False
#             if ord(word[i]) <= 90:
#                 flag = True # 대문자

#             tmp = ord(word[i]) + n
#             if tmp > 90 and flag:
#                 tmp -= 26
#             elif tmp > 122:
#                 tmp -= 26
#             else:
#                 pass
#             answer += str(chr(tmp))
#         answer += ' '
            
#     return answer[:-1]

def solution(s, n):
    answer = []
    for val in s:
        if val == ' ' :
            answer.append(' ')
        else :
            if val.islower(): # 소문자일 경우
                answer.append(chr((ord(val) - ord('a') + n) % 26 + ord('a')))
            elif val.isupper() : # 대문자일 경우
                answer.append(chr((ord(val) - ord('A') + n) % 26 + ord('A')))
            
    return ''.join(answer)