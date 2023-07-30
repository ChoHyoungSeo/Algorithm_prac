_ = int(input())
skills = list(map(str,input()))
complete = []
cnt = 0
for skill in skills:
    if skill == 'K':
        if 'S' in complete:
            cnt += 1
            complete.remove('S')
        else:
            break
    elif skill == 'R':
        if 'L' in complete:
            cnt += 1
            complete.remove('L')
        else:
            break
    elif skill == 'L':
        complete.append('L')
    elif skill == 'S':
        complete.append('S')
    else:
        cnt += 1
    
print(cnt)