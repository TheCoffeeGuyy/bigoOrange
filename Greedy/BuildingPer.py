n = int(input())

a = list(map(int, input().split()))
a.sort()
steps = 0
expect = 1
for ai in a:
    steps += abs(expect - ai)
    expect += 1
print(steps)