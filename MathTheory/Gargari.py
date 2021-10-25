class Cell:
    def __init__(self, x, y, m):
        self.x = x
        self.y = y
        self.m = m

def calculatePoint(row, col):
    point = matrix[row][col]
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        point += matrix[i][j]
        i -= 1
        j -= 1

    i = row + 1
    j = col + 1
    while i < n and j < n:
        point += matrix[i][j]
        i += 1
        j += 1

    i = row + 1
    j = col - 1
    while i < n and j >= 0:
        point += matrix[i][j]
        i += 1
        j -= 1

    i = row - 1
    j = col + 1
    while i >= 0 and j < n:
        point += matrix[i][j]
        i -= 1
        j += 1
    return point

n = int(input())

matrix = []
points = [[0] * n for i in range(n)]
for i in range(n):
    ith = list(map(int, input().split()))
    matrix.append(ith)

for i in range(n):
    for j in range(n):
        points[i][j] = calculatePoint(i, j)
max1 = x1 = y1 =0
for i in range(n):
    for j in range(n):
        if points[i][j] > max1:
            x1 = i
            y1 = j
            max1 = points[i][j]
max2 = x2 = y2 = 0
for i in range(n):
    for j in range(n):
        if points[i][j] > max2 and :
            x2 = i
            y2 = j
            max2 = points[i][j]

print(x1, y1, max1)
# print(points)