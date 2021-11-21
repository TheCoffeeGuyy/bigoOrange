def KMPPreprocess(p, prefix):
    m = len(p)
    j = 0
    i = 1
    while i < m:
        if p[i] == p[j]:
            j += 1
            prefix[i] = j
            i += 1
        else:
            if j != 0:
                j = prefix[j - 1]
            else:
                prefix[i] = 0
                i += 1

def KMPSearch(t, p, prefix):
    n = len(t)
    m = len(p)
    i = j = 0
    count = 0
    while i < n:
        if t[i] == p[j]:
            i += 1
            j += 1
        if j == m:
            count += 1
            j = prefix[j - 1]
        elif i < n and t[i] != p[j]:
            if j != 0:
                j = prefix[j - 1]
            else:
                i += 1
    return count

# tests = int(input())
# for i in range(1, tests + 1):
#     t = ''.join(input().split())
p = input()
prefix = [0] * len(p)
KMPPreprocess(p, prefix)
print(prefix)
#     print(f'Case {i}: {KMPSearch(t, p, prefix)}')