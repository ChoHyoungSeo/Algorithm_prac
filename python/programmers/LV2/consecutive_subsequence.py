def solution(elements):
    answer = set()
    elements *= 2
    for i in range(len(elements)//2):
        for j in range(len(elements)//2):
            answer.add(sum(elements[i:j+i]))
    return len(answer)