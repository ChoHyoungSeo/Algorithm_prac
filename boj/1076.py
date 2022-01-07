# 1076

tot_list = [['black', 0], ['brown', 1], ['red', 2], ['orange', 3], ['yellow', 4], ['green', 5], ['blue', 6], ['violet', 7], ['grey', 8], ['white', 9]]


fir = input()
sec = input()
mul = input()
ans = ''

for i in range(len(tot_list)):
    if fir == 'black':
        break
    if tot_list[i][0] == fir:
        ans += str(tot_list[i][1])

for i in range(len(tot_list)):
    if tot_list[i][0] == sec:
        ans += str(tot_list[i][1])

for i in range(len(tot_list)):
    if mul == 'black':
        break

    if ans =="0":
        ans = "0"
        break

    if tot_list[i][0] == mul:
        ans += str(10**tot_list[i][1])[1:]

print(ans)