n = 5
for i in range(n):
    print(' ' * (n - i), end='')
    c = 1
    for j in range(1, i + 2):
        print(c, end=' ')
        c = c * (i + 1 - j) // j
    print()
