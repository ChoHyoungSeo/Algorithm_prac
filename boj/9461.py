#9461
a = int(input())

for _ in range(a):
    tar = int(input())
    tmp=[1,1,1,2,2]
    cur_num = 2
    if tar <= 5:
        cur_num = tmp[tar-1]
   
    else:
        for i in range(tar-5):        
            cur_num += tmp[i]
            tmp.append(cur_num)
   
    print(cur_num)