while True:
    n = int(input())
    if n == 0:
        exit()
    a = list(map(int, input().split()))
    sells = [] # < 0
    buys = [] # > 0

    for i in range(n):
        if a[i] < 0:
            sells.append([a[i], i])
        else:
            buys.append([a[i], i])

    i = j = 0 
    ans = 0
    while i < len(sells) and j < len(buys):
        sum = sells[i][0] + buys[j][0]
        if sum == 0:
            # print('x',sells[i][1], buys[j][1], buys[j][0])
            ans += abs(sells[i][1] - buys[j][1]) * buys[j][0]
            i +=1 
            j +=1 
        elif sum > 0:
            # print('y',sells[i][1], buys[j][1], sells[i][0])
            ans += abs(sells[i][1] - buys[j][1]) * sells[i][0] * -1
            buys[j][0] =  sum
            i += 1
        else:
            # print('z',sells[i][1], buys[j][1], buys[j][0])
            ans += abs(sells[i][1] - buys[j][1]) * buys[j][0]
            sells[i][0] = sum
            j += 1
    print(ans)