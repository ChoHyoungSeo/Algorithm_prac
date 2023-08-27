n = int(input())
before = list(map(int, input()))
after = list(map(int, input()))
flag = False
if n % 2 == 0:
    if before == after:
        print("Deletion succeeded")
    else:
        print("Deletion failed")
else:
    for x, y in zip(before, after):
        if x == y:
            flag = True
            break
    if flag:
        print("Deletion failed")

    else:
        print("Deletion succeeded")