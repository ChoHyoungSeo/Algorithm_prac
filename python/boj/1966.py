# a = int(input())

# for _ in range(a):
#     tot, target = list(map(int, input().split()))
#     imp = list(map(int, input().split()))
#     idx = list(range(len(imp)))
#     idx[target] = 'target'
#     loc = 0
#     while True:
#         if imp[0] == max(imp):
#             loc += 1       
#             if idx[0] == 'target':
#                 print(loc)
#                 break
#             else:
#                 imp.pop(0)
#                 idx.pop(0)
#         else:
#             imp.append(imp.pop(0))
#             idx.append(idx.pop(0))

test_case = int(input())

for _ in range(test_case):
    n, m = list(map(int, input().split(' ')))
    queue = list(map(int, input().split(' ')))
    queue = [(i, idx) for idx, i in enumerate(queue)]
    
    count = 0
    while True:
        if queue[0][0] == max(queue, key=lambda x: x[0])[0]:
            count += 1
            if queue[0][1] == m:
                print(count)
                break
            else:
                queue.pop(0)
        else:
            queue.append(queue.pop(0))
            