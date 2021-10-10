k = 6

def combination (pieceOfAnswer, n, left, k):
    if k == 0:
        for j in range(len(pieceOfAnswer)):
            print(pieceOfAnswer[j], end=' ')
        print()
        return
    for i in range(left, n + 1):
        pieceOfAnswer.append(s[i])
        combination(pieceOfAnswer, n, i + 1, k - 1)
        pieceOfAnswer.pop()

while True:
    s = list(map(int, input().split()))
    if s[0] == 0:
        exit()

    pieceOfAnswer = []
    combination(pieceOfAnswer, len(s) - 1, 1, k)
    print()