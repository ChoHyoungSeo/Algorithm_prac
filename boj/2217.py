#2217
tot = int(input())
nums = []
candid = []
std = 0

for _ in range(tot):
    nums.append(int(input()))

nums.sort()
# 개수별로 봐주자

while std < tot:
    std += 1
    candid.append(nums[-std]*std)

print(max(candid))