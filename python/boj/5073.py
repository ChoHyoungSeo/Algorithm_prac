while True:
    nums = list(map(int, input().split()))
    if len(set(nums)) == 1 and nums[0] == 0:
        break
    nums.sort()
    if nums[0] + nums[1] <= nums[-1]:
        print('Invalid')
    elif len(set(nums)) == 1:
        print('Equilateral')
    elif len(set(nums)) == 2:
        print('Isosceles')
    elif len(set(nums)) == 3:
        print('Scalene')