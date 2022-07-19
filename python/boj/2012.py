tot = int(input())
tar_list = []
std_list = [x+1 for x in range(tot)]
cnt = 0

for i in range(tot):
    tar_list.append(int(input()))

tar_list.sort()
for i in range(tot):
    # cnt += abs(sorted(tar_list)[i] - std_list[i])
    cnt += abs(tar_list[i] - std_list[i])

print(cnt)

# #python으로 시간초과,,pypy로 정답
# n = int(input())
# expected = []
# for _ in range(n):
#     expected.append(int(input()))

# # 정렬
# expected.sort()

# # 불만족도 합
# result = 0
# for i in range(1, n+1):
#     result += abs(i-expected[i-1])
# print(result)


#정답
import sys
tot = int(sys.stdin.readline().strip())
tar_list = []
std_list = [x+1 for x in range(tot)]
cnt = 0

for i in range(tot):
    tar_list.append(int(sys.stdin.readline().strip()))

tar_list.sort()
for i in range(tot):
    # cnt += abs(sorted(tar_list)[i] - std_list[i])
    cnt += abs(tar_list[i] - std_list[i])
    
print(cnt)