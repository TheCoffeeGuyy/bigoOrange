def phi(n):
    result = 2
    temp = n
    count = 0
    for i in range(2, int(temp ** 0.5+1)):
        if temp % i == 0:
            count += 1
            result = max(result, i)   
            while temp % i == 0:
                temp /= i
    # print(count)
    # print('>',temp, count)
    if (temp == 1 and count == 1) or count == 0:
        return -1
    return int(max(result, temp))

while True:
    n = int(input())
    if n== 0:
        exit()
    print(phi(abs(n)))
    