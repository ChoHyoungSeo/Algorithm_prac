m, n = map(int, input().split())

def two_count(n):
    two = 0
    while n != 0:
        n = n // 2
        two += n
    return two

def five_count(n):
    five = 0
    while n != 0:
        n = n // 5
        five += n
    return five

print(min(two_count(m) - two_count(m - n) - two_count(n), five_count(m) - five_count(m - n) - five_count(n)))

# 0의 개수

# M!가 가지고 있는 2의 개수 - N!이 가지고 있는 2의 개수 - (M-N)!이 가지고 있는 2의 개수
# /
# M!가 가지고 있는 5의 개수 - N!이 가지고 있는 5의 개수 - (M-N)!이 가지고 있는 5의 개수
# 중에 작은 수

#timeover error
# def factorial(num):
#     if num == 0:
#         return 1
#     else:
#         ans = 1
#         for i in range(1,num+1):
#             ans *= i
#         return ans

# a,b = map(int, input().split())
# num = int((factorial(a)/(factorial(b)*factorial(a-b))))
# ans = 0
# num = str(num)[::-1]
# for i in range(len(num)):
#     if num[i] == "0":
#         ans += 1
#     else:
#         break
# print(ans)