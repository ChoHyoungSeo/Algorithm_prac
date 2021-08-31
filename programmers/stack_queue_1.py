from collections import Counter
def solution(progresses, speeds):
    answer = []
    i = 0
    ans_lis=[]
    while True:
        if i == len(progresses):
            break
        samp = progresses[i]
        samp_s = speeds[i]
        if ((100 - samp) % samp_s) == 0 :
            day = (100 - samp) // samp_s
        else:
            day = ((100 - samp) // samp_s) + 1
        try:
            tmp = ans_lis[i-1]
        except:
            tmp = day
        if day < tmp:
            day = tmp
        ans_lis.append(day)    
        i += 1

    ans_dict = dict(Counter(ans_lis).most_common(len(progresses)))
    for _, ans_num in enumerate(sorted(ans_dict.items())):
        answer.append(ans_num[1])
    return answer
