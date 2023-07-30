# def solution(s):
#     answer = []
#     ret = []
#     words = list(s)
#     for word in words:
#         answer.append(ord(word))
#     answer.sort(reverse=True)
#     for word in answer:
#         ret.append(chr(word))
#     return ''.join(ret)


def solution(s):
    return ''.join(sorted(s, reverse=True))