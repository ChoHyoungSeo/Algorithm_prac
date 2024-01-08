def solution(s, skip, index):
    answer = ''
    ascii_skip = [ord(word) for word in skip]
    for word in s:
        ascii_word = ord(word)
        for i in range(index):
            ascii_word += 1
            if ascii_word > 122:
                ascii_word -= 26
            while ascii_word in ascii_skip:
                ascii_word += 1
                if ascii_word > 122:
                    ascii_word -= 26
        answer += chr(ascii_word)
    return answer