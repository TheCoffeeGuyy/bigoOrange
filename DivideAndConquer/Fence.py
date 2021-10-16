import sys
sys.setrecursionlimit(10000)
n = int(input())

def paintFence(l, r, paintedHeight):

    if l > r:
        return 0
    indexOfMinHeight = l
    for i in range(l, r+ 1):
        if fences[i] < fences[indexOfMinHeight]:
            indexOfMinHeight = i
    horizontalStrokes = fences[indexOfMinHeight] - paintedHeight + paintFence(l, indexOfMinHeight - 1, fences[indexOfMinHeight]) + paintFence(indexOfMinHeight + 1, r, fences[indexOfMinHeight]) 

    return min(r - l + 1, horizontalStrokes)
fences = list(map(int, input().split()))

print(paintFence(0, n - 1, 0))