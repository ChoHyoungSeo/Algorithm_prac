def solution(s):
    ans = []
    s = s[2:-2]
    s_list = list(s.split('},{'))
    s_list.sort(key=len)
    for tar in s_list:
        int_tar = list(map(int, tar.split(',')))
        for num in int_tar:
            if num not in ans:
                ans.append(num)
    return ans