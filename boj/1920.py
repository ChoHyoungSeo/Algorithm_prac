#method 1.Set

# import sys
# n = sys.stdin.readline()
# N = set(sys.stdin.readline().split())
# m = sys.stdin.readline()
# M = sys.stdin.readline().split()

# for num in M:
#     sys.stdout.write('1\n') if num in N else sys.stdout.write('0\n')

###############################################
#method 2.binary search

# import sys
# n = sys.stdin.readline()
# N = sorted(map(int,sys.stdin.readline().split()))
# m = sys.stdin.readline()
# M = map(int, sys.stdin.readline().split())

# def binary(l, N, start, end):
#     if start > end:
#         return 0
#     m = (start+end)//2
#     if l == N[m]:
#         return 1
#     elif l < N[m]:
#         return binary(l, N, start, m-1)
#     else:
#         return binary(l, N, m+1, end)

# for l in M:
#     start = 0
#     end = len(N)-1
#     print(binary(l,N,start,end))

''' <in> operation (list) O(N)
time complexity of binary search O(logN)
<in> operation ,, Set or Dictionary data structure O(1)'''