# 정확도는 만점, 효율성은 0점
# def solution(participant, completion):
#     answer = ''
#     for name in completion:
#         participant.remove(name)
#     answer = participant[0]
#     return answer

#그게 그거
# def solution(participant, completion):
#     answer = ''
#     for name in participant:
#         if name in completion:
#             completion.remove(name)
#         else:
#             answer = name
#     return answer

#세번째 풀이 역시 앞에보다 훨씬 느림
# def solution(participant, completion):
#     answer = ''
#     p_dict = {}
#     for i in participant:
#         p_dict[i] = participant.count(i)
#     for name, num in p_dict.items():
#         for i in completion:
#             if name == i:
#                 num -= 1
#             else:
#                 continue
#         if num != 0:
#             answer = name
        
#     return answer

#All correct
#정확도 효율성 모두 만점

def solution(participant, completion):
    answer = ''
    p_dict = {}
    for name in participant:
        p_dict[name] = p_dict.get(name,0) + 1
    
    for name in completion:
        p_dict[name] -= 1
    
    for name in participant:
        if p_dict[name] != 0:
            answer = name
    return answer

# 백준에서 봤던 counter,,
# import collections
# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     return list(answer.keys())[0]