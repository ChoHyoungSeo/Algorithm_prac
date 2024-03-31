# #case 16: 0.87ms
# import numpy as np
# def solution(arr1, arr2):
#     return np.matmul(arr1,arr2).tolist()

# #case 16: 17.73ms
def solution(arr1, arr2):
    answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
    
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr2)):
                answer[i][j] += arr1[i][k] * arr2[k][j]
    
    return answer
