from itertools import permutations
def solution(babbling):
    answer = 0
    pool = ['aya', 'ye', 'woo', 'ma']
    word_pool = []
    
    for i in range(1, 5):
        word_pool.append(list(map(''.join, permutations(pool, r=i))))
    
    for bab in babbling:
        for word in word_pool:
            if bab in word:
                answer += 1
    return answer