# def selfNum(a: int) -> int :
#     v = a // 10000
#     w = (a - v*10000) // 1000
#     x = (a - v*10000 - w * 1000) // 100
#     y = (a - v * 10000 - w * 1000 - x * 100) // 10
#     z = (a - v * 10000 - w * 1000 - x * 100 - y * 10)
#     return a + v + w + x + y + z

# if __name__ == '__main__':
#     ans = [a for a in range(10000)]
#     for i in range(10000):
#         if selfNum(i) in ans:
#             ans.remove(selfNum(i))
#         else:
#             continue

#     for i in range(len(ans)):
#         print(ans[i], sep = '\n')

nums = [x+1 for x in range(10000)]
nonSelf = []

for num in nums:
  num = str(num)
  tmp = []
  for i in range(len(str(num))):
    tmp.append(int(num[i]))
  nonSelf.append((sum(tmp)+int(num)))

answer = set(nums) - set(nonSelf)
for ans in sorted(answer):
    print(ans)