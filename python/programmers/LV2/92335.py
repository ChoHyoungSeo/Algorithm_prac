from collections import deque
import math
def change_num(n,k):
    num = deque()
    while n > k:
        num.appendleft(str(n % k))
        n //= k 
    num.appendleft(str(n))
    return ''.join(num)
def solution(n, k):
    answer = 0
    n = change_num(n,k)
    nums = n.split('0')
    for num in nums:
        if not num or num == '1':
            continue
        num = int(num)
        is_prime=True
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                is_prime=False
                break
        if is_prime:
            answer += 1
        
    return answer