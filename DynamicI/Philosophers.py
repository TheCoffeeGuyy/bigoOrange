t = int(input())
for _ in range(t):
    h, w = map(int, input().split())
    matrix = []
    for j in range(h):
        line = list(map(int, input().split()))
        matrix.append(line)
    for j in range(1, h):
        for k in range(w):
            if k == 0:
                if w == 1:
                    matrix[j][k] += matrix[j-1][k]
                else:
                    matrix[j][k] += max(matrix[j-1][k], matrix[j-1][k+1])
            elif k == w - 1:
                matrix[j][k] += max(matrix[j-1][k-1], matrix[j-1][k])
            else:
                matrix[j][k] += max(matrix[j-1][k-1], matrix[j-1][k], matrix[j-1][k+1])
    # for a in matrix:
    #     print(a)
    print(max(matrix[h-1]))