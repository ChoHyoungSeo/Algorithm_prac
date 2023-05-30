def solution(name, yearning, photo):
    answer = []
    yearn_dict = {}
    for i in range(len(name)):
        yearn_dict[name[i]] = yearning[i]
    for group in photo:
        score = 0
        for person in group:
            if person in yearn_dict.keys():
                score += yearn_dict[person]
            else:
                continue
        answer.append(score)
    return answer