while True:
    std=[]
    cnt = 0
    for i in range(97, 123):
        std.append(chr(i))
    words = list(map(str, input()))
    if words[0] == '*':
        break
    for alp in std:
        if alp in words:
            cnt += 1
    if cnt == 26:
        print('Y')
    else:
        print('N')