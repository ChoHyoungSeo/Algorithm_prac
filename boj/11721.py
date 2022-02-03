#11721
a = input()

while True:
    try:
        if a:
            print(a[:10])
            a = a[10:]
        else:
            break
    except:
        print(a)
        break

# a = input()
# i = 0
# while i < len(a):
#     print(a[i:i+10])
#     i += 10