# from itertools import permutations
# n, m = map(int, input().split())
# nums = []
# for i in range(1, n+1):
#     for _ in range(m):
#         nums.append(i)
# for nums in sorted(list(set(permutations(nums, m)))):
#     print(*nums)

def dfs():
    if len(ans) == M:
        print(' '.join(map(str, ans)))
        return
    
    for i in range(1,N+1):
        ans.append(i)
        dfs()
        ans.pop()

if __name__ == '__main__':
    N, M = map(int, input().split())
    ans = []
    dfs()