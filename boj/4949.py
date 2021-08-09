while True:
    braket = []
    tmp = True
    line = input()
    if line == '.':
        break

    for fac in line:
        if fac == '(' or fac == '[':
            braket.append(fac)
        elif fac == ')':
            if not braket or braket[-1] == '[':
                tmp = False
                break
            elif braket[-1] == '(':
                braket.pop()
        elif fac == ']':
            if not braket or braket[-1] == '(':
                tmp = False
                break
            elif braket[-1] == '[':
                braket.pop()
    if tmp and not braket:
        print('yes')
    else:
        print('no')