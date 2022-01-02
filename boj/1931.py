#1931
tot = int(input())
time_list = []
ans = 0

#duration까지는 안구해도 되겠구나
#a,b = map(int, input().split())
#time_list.append([a,b,b-a])
for i in range(tot):
    time_list.append(list(map(int, input().split())))

#최대한 많이하려면 일단 일찍 끝나는애로
time_list.sort(key = lambda x: (x[1], x[0]))

end_time = time_list[0][1]
for i in range(1, tot): 
    if time_list[i][0] >= end_time: 
        ans += 1 
        end_time = time_list[i][1]

print(ans+1)