
# 다음 도시만 보는건 최적의 해가 아니다.
# 17점

# tot_city = int(input())
# lengthOfCity = list(map(int, input().split()))
# costOfFuel = list(map(int, input().split()))
# ans = 0 #total cost
# tick = 0

# ans += costOfFuel[0] * lengthOfCity[0]

# for i in range(1, len(costOfFuel)-1):
#     if tick == 1:
#         tick = 0
#         continue

#     if costOfFuel[i] < costOfFuel[i+1]:
#         ans += costOfFuel[i] * (lengthOfCity[i] + lengthOfCity[i+1])
#         tick = 1

#     else:
#         ans += costOfFuel[i] * lengthOfCity[i]

# print(ans)


# 값을 기억해줘야 하고 초기값도 일반화 될 것을 생각
# 100점
tot_city = int(input())
lengthOfCity = list(map(int, input().split()))
costOfFuel = list(map(int, input().split()))
ans = 0 #total cost

# if costOfFuel[0] == min(costOfFuel):
#     ans += sum(lengthOfCity) * costOfFuel[0]

for i in range(len(costOfFuel)-1):

    if costOfFuel[i] < costOfFuel[i+1]:
        costOfFuel[i+1] = costOfFuel[i]
    
    ans += costOfFuel[i] * lengthOfCity[i]

print(ans)