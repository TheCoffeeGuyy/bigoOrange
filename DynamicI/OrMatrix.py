m, n = map(int, input().split())
b = []
a = [[1] * n for i in range(m)]
for i in range(m):
    line = list(map(int, input().split()))
    b.append(line)

for i in range(m):
    for j in range(n):
        if b[i][j] == 0:
            for k in range(n):
                a[i][k] = 0
            for k in range(m):
                a[k][j] = 0

convertable = True
for i in range(m):
    for j in range(n):
        if b[i][j] == 1:
            found = False
            for k in range(n):
                if a[i][k] == 1:
                    found = True
            for k in range(m):
                if a[k][j] == 1:
                    found = True
            if not found:
                convertable = False
if convertable:
    print('YES')

    for ai in a:
        for aij in ai:
            print(aij, end=' ')
        print()
else:
    print('NO')