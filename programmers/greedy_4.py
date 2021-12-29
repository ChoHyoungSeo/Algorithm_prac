#구명보트
#only 75
#should avoid time error
#정확도 만점, 효율성 0,,?
# from collections import deque

# def solution(people, limit):
#     answer = 0
#     people.sort(reverse=True)
#     people = deque(people)
    
#     while True:
#         if not people:
#             break
            
#         person = people[0]
#         people.popleft()
#         for i in range(len(people)):
#             if people[i] + person <= limit:
#                 del people[i]
#                 break
#             else:
#                 continue
#         answer += 1
    
#     return answer

#반대로 돌려도 똑같아 도중에 브레이크를 걸어줘도 안되네
# binary search 를 해야하나
# from collections import deque

# def solution(people, limit):
#     answer = 0
#     people.sort()
#     people = deque(people)
    
#     while True:
#         if not people:
#             break
            
#         person = people[-1]
#         people.pop()
#         for i in range(len(people)):
#             if people[i] + person <= limit:
#                 del people[i]
#                 break
#             else:
#                 continue
#         answer += 1
    
#     return answer

from collections import deque
def solution(people, limit):
    answer = 0
    people.sort()
    people = deque(people)

    while True:
        if not people:
            break
            
        person = people[-1]
        people.pop()
        print(people)
        print(answer)
        try:
            if people[0] + person <= limit:
                people.popleft()
        except:
            answer += 1
            break
        
        answer += 1

    return answer

if __name__ == "__main__":
    people = [70,80,50]
    limit = 100
    print(solution(people, limit))

# 가장 무거운 친구와 가장 가벼운 친구 까지만 고려
# 정확도 만점, 효율성 만점
from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    people = deque(people)

    while True:
                
        if not people:
            break
            
        person = people[-1]
        people.pop()
        
        try:
            if people[0] + person <= limit:
                people.popleft()
                
        except:
            answer += 1
            break

        answer += 1

    return answer
