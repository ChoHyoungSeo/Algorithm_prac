def solution(n, arr1, arr2):
    answer = []
    pool1 = []
    pool2 = []
    for num in arr1:
        pool1.append(bin(num)[2:].zfill(n))
    for num in arr2:
        pool2.append(bin(num)[2:].zfill(n))
    for x, y in zip(pool1, pool2):
        tmp = ""
        for i in range(n):
            if x[i] == "1" or y[i] == "1":
                tmp += "#"
            else:
                tmp += " "
        answer.append(tmp)

    return answer