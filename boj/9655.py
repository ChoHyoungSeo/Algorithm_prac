#9655 game theory

stone = int(input())
if (stone - 1) % 4 == 0 or (stone-3) % 4 == 0:
    print("SK")
else:
    print("CY")