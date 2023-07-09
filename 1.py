a = input().split(' ')
b = ('а', 'я', 'у', 'ю', 'о', 'е', 'ё', 'э', 'и', 'ы')
d = []

for i in range(len(a)):
    count1 = 0
    for j in range(len(a[i])):
        if a[i][j] in b:
            count1 += 1
    d.append(count1)

for j in range(len(d)):
    if d[0] == d[j]:
        print('Парам пам-пам')
    else:
        print('Пам парам')
