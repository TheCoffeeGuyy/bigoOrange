import math

n, m = map(int, input().split())

listb = list(map(int, input().split()))
happyBoys = [False] * n
for x in listb[1:]:
    happyBoys[x] = True

listg = list(map(int, input().split()))
happyGirls = [False] * m
for x in listg[1:]:
    happyGirls[x] = True

days = m*n/math.gcd(n,m)

for i in range(int(days)):
    ithBoy = i % n
    ithGirl = i % m
    if happyBoys[ithBoy] or happyGirls[ithGirl]:
        happyBoys[ithBoy] = happyGirls[ithGirl] = True

count = 0

for i in range(n):
    if happyBoys[i]:
        count += 1
for i in range(m):
    if happyGirls[i]:
        count += 1

if count == (n+m):
    print('Yes')
else: print('No')