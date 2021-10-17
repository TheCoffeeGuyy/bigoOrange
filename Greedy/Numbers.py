k = int(input())
n = list(map(int, input()))
curSum = 0
for i in n:
    curSum += i
ans = 0
n.sort()
while curSum < k:
    curSum += 9 - n[ans]
    ans += 1
print(ans)