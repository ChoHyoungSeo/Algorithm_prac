even_chess = []
odd_chess = []
cnt = 0

for i in range(1, 9):
    if i % 2 == 0:
        even_chess.append(input())
    else:
        odd_chess.append(input())

for col in even_chess:
    for i in range(len(col)):
        if i % 2 == 0 :
            continue
        else:
            if col[i] == 'F':
                cnt += 1

for col in odd_chess:
    for i in range(len(col)):
        if i % 2 == 0:
            if col[i] == 'F':
                cnt += 1

print(cnt)