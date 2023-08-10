sem, maj, tot = map(int, input().split())
minor = tot - maj
study = []
for i in range(10):
    study.append(list(map(int, input().split())))
for i in range(8 - sem):
    n_maj, n_minor = study[i]
    rest_cre = 6

    maj += (n_maj * 3)
    rest_cre -= n_maj
    if n_minor <= rest_cre:
        minor += (n_minor * 3)
    else:
        minor += (rest_cre * 3)

if maj + minor >= 130 and maj >= 66:
    print("Nice")
else:
    print("Nae ga wae")