def solution(s):
    answer = ''
    words = list(map(str, s.split(' ')))
    print(words)
    for word in words:
        if word:
            if word[0] and word[0].isalpha():
                answer += word[0].upper()
            else:
                answer += word[0]
            if len(word) > 1:
                for i in range(1, len(word)):
                    if word[i].isalpha():
                        answer += word[i].lower()
                    else:
                        answer += word[i]
        answer += ' '
        
    return answer[:-1]

# python library has JadenCase func