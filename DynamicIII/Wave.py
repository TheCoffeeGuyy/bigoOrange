while True:
    try:
        n = int(input())
        increase = [1] * (n)
        decrease = [1] * (n)
        a = list(map(int, input().split()))
        lena = len(a)
        for i in range(1, lena):
            for j in range(i):
                if a[i] > a[j]:
                    increase[i] = max(increase[i], increase[j] + 1)
        a.reverse()
        for i in range(1, lena):
            for j in range(i):
                if a[i] > a[j]:
                    decrease[i] = max(decrease[i], decrease[j] + 1)
        maxx = 1
        for i in range(lena):
            minn = min(decrease[i], increase[i])
            maxx = max(maxx, minn * 2 - 1)
        print(maxx)

    except EOFError:
        exit()