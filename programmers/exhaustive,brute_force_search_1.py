#should improve / only temporary measure
def solution(answers):
    answer = []
    stud1 = "12345"
    stud2 = "21232425"
    stud3 = "3311224455"
    answers = list(map(str, answers))
    cnt = []
    tmp1 = 0
    tmp2 = 0
    tmp3 = 0
    stud1 *= (len(answers)//5 + 1)
    stud2 *= (len(answers)//5 + 1)
    stud3 *= (len(answers)//5 + 1)
    for i in range(len(answers)):
        if stud1[i] == answers[i]:
            tmp1 += 1
        if stud2[i] == answers[i]:
            tmp2 += 1
        if stud3[i] == answers[i]:
            tmp3 += 1
    cnt.append(tmp1)
    cnt.append(tmp2)
    cnt.append(tmp3)
    m_tmp = max(cnt)
    for i in range(len(cnt)):
        if cnt[i] == m_tmp:
            answer.append(i+1)
    
    return answer