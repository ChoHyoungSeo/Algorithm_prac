#improve?

from collections import deque

def solution(priorities, location):
    ans = 1
    priorities = deque(priorities)
    if priorities[location] == max(priorities):
        for i in range(location):
            if priorities[i] == priorities[location]:
                ans += 1
            else:
                continue
        return ans
    else:
        while True:
            if priorities[location] != max(priorities):
                if priorities[0] == max(priorities):
                    priorities.popleft()
                    ans += 1
                    location -= 1
                else:
                    priorities.append(priorities[0])
                    priorities.popleft()
                    location -= 1
                    
                if location < 0:
                    location = len(priorities) - 1
                    
            else:
                break
                
        for i in range(location):
            if priorities[i] == priorities[location]:
                ans += 1
            else:
                continue
    return ans