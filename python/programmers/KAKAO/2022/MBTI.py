def solution(survey, choices):
    ans = ''
    std_dict = {"R":0, "T":0, "C":0, "F":0, "J":0, "M":0, "A":0, "N":0}
    
    for prob, score in zip(survey, choices):
        if score == 4:
            pass
        elif score == 3:
            std_dict[prob[0]] += 1
        elif score == 2:
            std_dict[prob[0]] += 2
        elif score == 1:
            std_dict[prob[0]] += 3
        elif score == 5:
            std_dict[prob[1]] += 1
        elif score == 6:
            std_dict[prob[1]] += 2
        elif score == 7:
            std_dict[prob[1]] += 3
    if std_dict['R'] >= std_dict['T']:
        ans += 'R'
    else:
        ans += 'T'
    if std_dict['C'] >= std_dict['F']:
        ans += 'C'
    else:
        ans += 'F'
    if std_dict['J'] >= std_dict['M']:
        ans += 'J'
    else:
        ans += 'M'
    if std_dict['A'] >= std_dict['N']:
        ans += 'A'
    else:
        ans += 'N'
    
    return ans