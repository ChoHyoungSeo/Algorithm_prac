tot = int(input())
postfix = input()
nums = {chr(ord('A') + i): int(input()) for i in range(tot)}
stack = []

for char in postfix:
    if char.isalpha():
        stack.append(nums[char])
    else:
        b = stack.pop()
        a = stack.pop()

        if char == "+":
            stack.append(a + b)
        elif char == '-':
            stack.append(a - b)
        elif char == "*":
            stack.append(a * b)
        else:
            stack.append(a / b)

print(f"{stack[0]:.2f}")