k = int(input())

def check (visited, row, col):
    for i in range(row):
        if visited[i][col]:
            return False
    i = row
    j = col

    while i >=  0 and j >= 0:
        if visited[i][j]:
            return False
        i -=1 
        j -= 1
    
    i = row
    j = col
    while j < 8 and i >= 0:
        if visited[i][j]:
            return False
        i -=1
        j += 1
    
    return True

def nQueens(visited, row, ans):
    if row == 8:
        res = 0
        for i in range(8):
            for j in range(8):
                if visited[i][j]:
                    res += boards[i][j]
        ans.append(res)
        return True
    for j in range(8):
        if check(visited, row, j) == True:
            visited[row][j] = True
            nQueens(visited, row+1, ans)
            visited[row][j] = False
    
    return False


for _ in range(k):
    boards = []
    visited = [[False] * 8 for i in range(8)] 
    for i in range(8):
        line = list(map(int, input().split()))
        boards.append(line)
    ans = []
    nQueens(visited, 0, ans)
    res = max(ans)
    r = ''
    if len(str(res)) < 5:
        for i in range(5 - len(str(res))):
            r += ' '
    r += str(res)
    print(r)