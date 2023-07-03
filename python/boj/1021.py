
# #dummy 가 꼭 필요할까?
# from collections import deque

# #앞에를 뒤로
# def push_head(dummy_numbers: deque) -> deque:
#     dummy_numbers.append(dummy_numbers[0])
#     dummy_numbers.popleft()
#     return dummy_numbers

# #뒤에서 앞으로 
# def push_tail(dummy_numbers: deque ) -> deque:
#     dummy_numbers.appendleft(dummy_numbers[-1])
#     dummy_numbers.pop()
#     return dummy_numbers

# if __name__ == '__main__':

#     tot, num_of_target = map(int, input().split())
#     target_num = list(map(int, input().split()))
#     ans = 0
#     dummy_numbers = [x for x in range(1, tot+1)]
#     dummy_numbers = deque(dummy_numbers)

#     for num in target_num:
#         while dummy_numbers[0] != num:
#             if dummy_numbers.index(num) > int(len(dummy_numbers)/2):
#                 dummy_numbers = push_tail(dummy_numbers)
#                 ans += 1

#             elif dummy_numbers.index(num) <= int(len(dummy_numbers)/2):
#                 dummy_numbers = push_head(dummy_numbers)
#                 ans += 1

#             if dummy_numbers[0] == num:
#                 break
            
#         dummy_numbers.popleft()
#     print(ans)
import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int, input().split())
d = deque([i for i in range(1, n+1)])
targets = list(map(int, input().split()))
cnt = 0

for target in targets:
    index = d.index(target)
    if index <= len(d) // 2:
        for i in range(index):
            x = d.popleft()
            d.append(x)
            cnt += 1
    else:
        for i in range(len(d) - index):
            x = d.pop()
            d.appendleft(x)
            cnt += 1
    d.popleft()
print(cnt)
            