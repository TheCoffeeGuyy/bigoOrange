moves = [[-2, -1], [-2, 1], [-1, -2], [-1, 2], [1,-2], [1,2], [2,-1], [2,1]]
m = 10

def backtrack(r, c):
    path = 0
    graph[r][c] = 'X'
    for move in moves:
        dr = r+ move[0]
        dc = c+ move[1]
        if dr in range(m) and dc in range(m) and graph[dr][dc] == '.':
            path = max(path, backtrack(dr,dc))
    graph[r][c] = '.'

    return path + 1

test = 1
while True:
    n = list(map(int, input().split()))
    if n[0] == 0:
        exit()
    graph = []
    total = 0
    for ith in range(1, n[0] * 2, 2):
        line = []
        for i in range(n[ith]):
            line.append('X')
        for i in range(n[ith+1]):
            total +=1
            line.append('.')
        for i in range(m- n[ith+1] - n[ith]):
            line.append('X')
        graph.append(line)
    for i in range(m - n[0]):
        graph.append(['X' for _ in range(m)])

    visited = [[False for i in range(m)] for i in range(m)]
    startR = 0
    startC = -1
    for i in range(10):
        if graph[0][i] == '.':
            startC = i
            break
    res = total-backtrack(startR, startC)
    square = 'square' if res == 1 else 'squares'
    print(f'Case {test}, {res} {square} can not be reached.')
    test += 1
