from collections import Counter

def solution(topping):
    ans = 0
    right = Counter(topping)
    left = set()
    
    for t in topping:
        right[t] -= 1
        left.add(t)
        
        if right[t] == 0:
            right.pop(t)
            
        if len(right) == len(left):
            ans += 1
    return ans