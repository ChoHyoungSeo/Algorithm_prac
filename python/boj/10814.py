a = int(input())
people = []

for _ in range(a):
    people.append((input().split()))

people.sort(key= lambda x : int(x[0]))
for i in range(a):
    print(people[i][0] +" "+ people[i][1])
