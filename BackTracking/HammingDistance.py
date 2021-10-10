t = int(input())
input()
def shouldSwap(s, start, end):
    for i in range(start, end):
        if s[i] == s[end]:
            return False
    return True

def distinctPermutions(s, l, r):
    if l >= r:
        print(''.join(s))
        return
    
    for i in range(l, r):
        if shouldSwap(s, l, i):
            s[i], s[l] = s[l], s[i]
            distinctPermutions(s, l+1, r)
            s[i], s[l] = s[l], s[i]

for i in range(t):
    n, h = map(int, input().split())
    if i != t - 1:
        input()
    s = []
    for i in range(n - h):
        s.append('0')
    for i in range(h):
        s.append('1')

    distinctPermutions(s, 0, len(s))
    if i == t - 1:
        print()