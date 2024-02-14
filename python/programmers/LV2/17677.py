from collections import Counter
def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    pool1, pool2 = [], []
    inter, uni = 0, 0
    
    for i in range(len(str1)-1):
        tmp = str1[i:i+2]
        if tmp.isalpha():
            pool1.append(tmp)
    for i in range(len(str2)-1):
        tmp = str2[i:i+2]
        if tmp.isalpha():
            pool2.append(tmp)
    
    pool1_dict = Counter(pool1)
    pool2_dict = Counter(pool2)
    
    inter = list((pool1_dict & pool2_dict).elements())
    uni = list((pool1_dict | pool2_dict).elements())
    
    return int((len(inter)/len(uni)) * 65536) if len(uni) != 0 else 65536