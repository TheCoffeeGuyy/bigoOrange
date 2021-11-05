n = int(input())

a = list(map(int, input().split()))
dic = {}
flag = False
for e in a:
    el = list(map(int, str(e)))
    f = e ^ sum(el)
    if f in dic:
        flag = True
        dic[f] += 1
    else:
        dic[f] = 0
if flag:
    key = max(dic, key=lambda k: dic[k])
    print(key, dic[key])
else:
    print(max(dic, key=lambda k: k), 0)

for i in dic:
    print(dic, dic[i])