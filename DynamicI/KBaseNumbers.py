n = int(input())
k = int(input())

if n == 1:
    print(k)
else:
    endWith0 = [0]*20
    endWithout0 = [0]*20
    endWithout0[1] = k-1
    for i in range(2, n+1):
        endWith0[i] = endWithout0[i-1]
        endWithout0[i] = (endWithout0[i-1] + endWith0[i - 1]) * (k-1)
    print(endWithout0[n]+ endWith0[n])