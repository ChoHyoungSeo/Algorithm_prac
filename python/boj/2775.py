# def pnum(a:int, b:int) -> int:
#     if a == 0:
#         return b
#     if b == 1:
#         return 1
#     else:
#         return pnum(a, b-1) + pnum(a-1, b)

# if __name__ == '__main__':
#     q = int(input())

#     for i in range(q):
#         r = int(input())
#         w = int(input())

#         print(pnum(r,w))
t = int(input())

for i in range(t):
    k = int(input())        # 층
    n = int(input())        # 호
    people = [i for i in range(1, n+1)]     # 0층

    for x in range(k):
        new = []
        for y in range(n):
            new.append(sum(people[:y+1]))   # 아래층의 1~n호 까지의 합
        people = new.copy()
    print(people[-1])