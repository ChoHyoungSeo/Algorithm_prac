from collections import deque

def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    
    answer = 0
    my_list = deque(maxlen=cacheSize)
    
    for city in cities:
        city = city.lower()
        if city in my_list:
            answer += 1
            my_list.remove(city)
            my_list.append(city)
        else:
            answer += 5
            if len(my_list) >= cacheSize:
                my_list.popleft()
            my_list.append(city)
    return answer