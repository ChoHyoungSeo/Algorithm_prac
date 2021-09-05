#temp
N, A_M = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

B_M, K = map(int, input().split())
B = []
for _ in range(B_M):
    B.append(list(map(int, input().split())))
    
result = []

for A_subset in A:
    B_subset = [0] * K
    for i, ele in enumerate(A_subset):
        target_subset = [ele * num for num in B[i]]
        B_subset = [sum(x) for x in zip(B_subset, target_subset)]
    result.append(B_subset)
    
for row in result:
    print(*row)