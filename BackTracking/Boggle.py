VOWELS = "AEOYIU"
DIRs = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, -1], [1, -1], [-1, 1]]

def backtrack(word, r, c,boggle, store):
    visited[r][c] = True
    word += boggle[r][c]
    if len(word) == 4:
        countVowel = 0
        for w in word:
            if w in VOWELS:
                countVowel+= 1
        if countVowel == 2:
            store.add(word)
    else:
        for dir in DIRs:
            dr = dir[0] + r
            dc = dir[1] + c
            if dr in range(4) and dc in range(4) and not visited[dr][dc]:
                backtrack(word, dr, dc, boggle, store)
    visited[r][c] = False

while True:
    boggle1 = []
    set1 = set()
    boggle2 = []
    set2 = set()
    for _ in range(4):
        line = input().split()
        if line[0] == '#':
            exit()
        boggle1.append(line[0:4:])
        boggle2.append(line[4::])
    visited = [[False for _ in range(4)] for _ in range(4)]

    for i in range(4):
        for j in range(4):
            word = ''
            backtrack(word, i, j, boggle1, set1)
    for i in range(4):
        for j in range(4):
            word = ''
            backtrack(word, i, j, boggle2, set2)
    res = []
    for x in set1:
        if x in set2:
            res.append(x)
    res.sort()
    if len(res) == 0:
        print('There are no common words for this pair of boggle boards.')
    else: 
        for r in res:
            print(r)
    print()

    # print answer

    input()

