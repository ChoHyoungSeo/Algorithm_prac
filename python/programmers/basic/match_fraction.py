# use euclidean
# check if divisible after sum operation

def gcd(x, y):
    while y:
        x,y = y,x%y
    return x

def lcm(x, y):
    result = (x*y)//gcd(x,y)
    return result

def solution(numer1, denom1, numer2, denom2):
    answer = []
    lcm_num = lcm(denom1, denom2)
    ans1 = numer1 * (lcm_num // denom1) + numer2 * (lcm_num // denom2)
    gcd_num = gcd(ans1, lcm_num)
    ans = ans1 // gcd_num
    answer.append(ans)
    answer.append(lcm_num // gcd_num)
    return answer