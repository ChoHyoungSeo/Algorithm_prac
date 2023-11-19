def solution(want, number, discount):
    answer = 0

    for i in range(len(discount)-9):
        tmp = discount[i:i+10]
        pool = [w for w, n in zip(want, number) for _ in range(n)]
        for product in tmp:
            if product not in pool:
                break
            else:
                pool.remove(product)
        if not pool:
            answer += 1
    return answer
