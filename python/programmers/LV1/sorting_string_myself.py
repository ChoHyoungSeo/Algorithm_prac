# def solution(strings, n):
#     answer = []
#     ans_dict = {}
    
#     for i in range(len(strings)):
#         ans_dict[ord(strings[i][n])] = []
    
#     for i in range(len(strings)):
#         ans_dict[ord(strings[i][n])].append(strings[i])
    
#     ans_dict = sorted(ans_dict.items())
#     for candid in ans_dict:
#         if len(candid[-1]) > 1:
#             candid[-1].sort()
#         for can in candid[-1]:
#             answer.append(can)
    
#     return answer

def solution(strings, n):
    return sorted(strings, key=lambda x:(x[n],x))