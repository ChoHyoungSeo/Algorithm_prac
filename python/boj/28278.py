import sys
input = sys.stdin.readline

n = int(input())
nums = []
for _ in range(n):
    
    cmds = list(map(str, input().split()))
    if len(cmds) != 1:
        num = int(cmds[-1])
    cmd = int(cmds[0])
    if cmd == 1:
        nums.append(num)
    elif cmd == 2:
        if nums:
            print(nums.pop())
        else:
            print(-1)
    elif cmd == 3:
        print(len(nums))
    elif cmd == 4:
        if nums:
            print(0)
        else:
            print(1)
    else:
        if nums:
            print(nums[-1])
        else:
            print(-1)