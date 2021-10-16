while True:
    n = int(input())
    if n == 0:
        exit()
    flag = 1
    a = 0
    b = 0
    for i in range(32):
        if (n >> i) & 1:
            if flag:
                a += 1 << i
                # flag = ~flag
            else:
                b += 1 << i
                # flag = ~flag

            flag ^= 1
    print(a, b)