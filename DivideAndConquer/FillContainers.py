def fillable(capacity, vessels, m):
    container = 0
    numberOfContainers = 0
    for c in vessels:
        if c > capacity:
            return False
        if container + c > capacity:
            container = 0
        if container == 0:
            numberOfContainers +=1 
        if numberOfContainers > m:
            return False
        container += c
        
    return True

def binarySearch(total, vessels, m):
    left = 0
    right = total
    res = -1
    while left <= right:
        mid = (left+right) // 2
        if fillable(mid, vessels, m):
            right = mid - 1
            res = mid
        else:
            left = mid + 1
    return res

while True:
    try:
        n, m = map(int, input().split())
        vessels = list(map(int, input().split()))

        ans = binarySearch(sum(vessels), vessels, m)
        print(ans)
    except EOFError as e:
        exit()