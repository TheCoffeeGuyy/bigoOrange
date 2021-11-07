t = int(input())
for _ in range(t):
    strr = input()
    patt = input()
    dic = {}
    for i in range(len(strr)):
        if strr[i] not in dic:
            dic[strr[i]] = i
    minId = 100000
    for c in patt:
        if c in dic:
            minId = min(minId, dic[c])
    if minId != 100000:
        print(strr[minId])
    else:
        print('No character present')