#list 활용하면 시간초과
n = int(input())
chats = set()
cnt = 0
for _ in range(n):
    chat = input()

    if chat != 'ENTER':
        if chat not in chats:
            cnt += 1
            chats.add(chat)

    elif chat == 'ENTER':
        chats = set()
print(cnt)