test = 1
while True:
    a = []
    ai = int(input())
    if ai == -1:
        break
    if test == 1:
        print()
    a.append(ai)
    while True:
        ai = int(input())
        if ai == -1:
            break
        a.append(ai)
    lena = len(a)
    f = [1] * (lena + 1)
    ans = 1
    for i in range(1, lena):
        for j in range(i):
            if a[i] <= a[j]:
                f[i] = max(f[i], f[j] + 1)
        ans = max(ans, f[i])
    print(f'Test #{test}:')
    print(f'  maximum possible interceptions: {ans}')
    test += 1

    