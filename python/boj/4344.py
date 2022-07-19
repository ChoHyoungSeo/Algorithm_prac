a = int(input())

for i in range(a):
    score = list(map(int, input().split()))
    rscore = score[1:]
    avg = sum(rscore)/len(rscore)
    cnt = 0
    
    for j in range(len(rscore)):
        if rscore[j] > avg :
            cnt += 1
        
        else:
            continue

    print(str("%.3f" %((cnt/len(rscore)) * 100)) + "%")