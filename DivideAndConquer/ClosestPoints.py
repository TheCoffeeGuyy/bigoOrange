class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

def distance(p1, p2):
    x = p1.x - p2.x
    y = p1.y - p2.y

    return (x * x + y * y) ** 0.5

def bruteForce(points, left, right):
    minDist = 1e9

    for i in range(left, right):
        for j in range(i +1, right):
            minDist = min(minDist, distance(points[i], points[j]))
    return minDist

def stripClosest(pointsSet, l, r, mid, disMin):
    midPoint = pointsSet[mid]
    inRangePoints = []

    for i in range(l, r):
        if abs(midPoint.x - pointsSet[i].x) < disMin:
            inRangePoints.append(pointsSet[i])
    
    inRangePoints.sort(key=lambda point: point.y)

    smallestDis = disMin

    for i in range(0, len(inRangePoints)):
        for j in range(i+1, len(inRangePoints)):
            if not inRangePoints[j].y - inRangePoints[i].y < disMin:
                break
            d = distance(inRangePoints[j], inRangePoints[i])
            smallestDis = min(smallestDis, d)
    
    return smallestDis

def minimalDistance(pointsSet, l, r):
    if r - l <= 3:
        return bruteForce(pointsSet,l, r)
    
    mid = (l + r) // 2
    disLeft = minimalDistance(pointsSet, l, mid)
    disRight = minimalDistance(pointsSet, mid + 1, r)
    disMin = min(disLeft, disRight)
    return min(disMin, stripClosest(pointsSet, l, r, mid, disMin))
    
while True:

    n = int(input())
    if n == 0:
        exit()
    pointsSet = []

    for i in range(n):
        x, y = map(int, input().split())
        pointsSet.append(Point(x, y))

    pointsSet.sort(key = lambda point: point.x)

    ans = minimalDistance(pointsSet, 0, n)

    if ans < 10000:
        print('{:.4f}'.format(ans))
    else:
        print('INFINITY')