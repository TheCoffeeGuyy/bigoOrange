s1 = input()
s2 = input()

s1Count = 0
for s in s1:
    if s == '+':
        s1Count += 1
    elif s == '-':
        s1Count -= 1
s2Count = 0
for s in s2:
    if s == '+':
        s2Count += 1
    elif s == '-':
        s2Count -= 1

dif = s2Count - s1Count

