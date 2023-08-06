from collections import deque
import sys
input = sys.stdin.readline

tot = int(input())
nums = deque()
for _ in range(tot):
    cmds = list(map(int, input().split()))
    if cmds[0] == 1:
        nums.appendleft(cmds[-1])
    elif cmds[0] == 2:
        nums.append(cmds[-1])
    elif cmds[0] == 3:
        if not nums:
            print(-1)
        else:
            print(nums.popleft())
    elif cmds[0] == 4:
        if not nums:
            print(-1)
        else:
            print(nums.pop())
    elif cmds[0] == 5:
        print(len(nums))
    elif cmds[0] == 6:
        if nums:
            print(0)
        else:
            print(1)
    elif cmds[0] == 7:
        if not nums:
            print(-1)
        else:
            print(nums[0])
    elif cmds[0] == 8:
        if not nums:
            print(-1)
        else:
            print(nums[-1])