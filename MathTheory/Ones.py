while True:
    try:
        n = int(input())
        i = 1
        tmp = 1
        while True:
            if tmp % n == 0:
                break
            tmp = tmp*10+1
            i+=1
        print(i)
    except EOFError:
        exit()