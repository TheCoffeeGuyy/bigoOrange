class Person:
    def __init__(self, b, s, index):
        self.b = b
        self.s = s
        self.index = index + 1
    
    def __lt__(self, other):
        if self.b == other.b:
            return other.s > self.s
        return self.b > other.b 

def lowerBound (a, sub, n, x):
    left = 0
    right = n
    pos = right
    while left < right:
        mid = int((left + right)/2)
        index = sub[mid]
        if a[index].s >= x.s:
            right = mid
            pos = mid
        else:
            left = mid + 1
    return pos
n = int(input())
a = []
for i in range(n):
    b, s = map(int, input().split())
    a.append(Person(b, s, i))
a.sort(reverse=True)
for ai in a:
    print(ai.b, ai.s,)
# LIS
length = 1
dp = [0]
for i in range(1, len(a)):
    if a[i].s <= a[dp[0]].s:
        dp[0] = i 
    elif a[i].s > a[dp[length - 1]].s:
        length += 1
        dp.append(i)
    else:
        pos = lowerBound(a, dp, length, a[i])
        dp[pos] = i

print(length)
print(dp)
for d in dp:
    print(a[d].b, a[d].s, a[d].index)

# class Member:
#   def __init__(self,s,b,_id):
#     self.s = s
#     self.b = b
#     self._id = _id
#   def __lt__(self,other):
#     if self.s == other.s:
#       return self.b > other.b
#     return self.s < other.s
#   def __str__(self):
#     return str(self.s)+ " "+str(self.b) + \
#     " " + str(self._id)

# def lower_bound(a,sub,n,x):
#   left = 1
#   right = n
#   pos = right
#   while left < right:
#     mid = int((left + right)/2)
#     index = sub[mid]
#     if a[index].b >= x:
#       pos = mid
#       right = mid
#     else:
#       left = mid + 1
#   return pos


  
# def LIS(a):
#   res = []
#   length = 1
#   increasingSub = [0 for i in range(len(a))]
#   path = [-1 for i in range(len(a))]
#   increasingSub[1] = 1

#   for i in range(2,len(a)):
#     if a[i].b > a[increasingSub[length]].b :
#       length += 1
#       increasingSub[length] = i
#       path[i] = increasingSub[length - 1]
#     else:
#       pos = lower_bound(a, increasingSub, length, a[i].b)
#       path[i] = increasingSub[pos - 1]
#       increasingSub[pos] = i

#   i = increasingSub[length];
#   print(increasingSub)
#   while i > 0 :
#     res.append(a[i]._id);
#     i = path[i];
    
#   return length,res

# def main():
#   n = 0
#   #a,b,c = list(map(int, input().split()))
#   n = int(input())
#   members = [0,]
#   for i in range(1,n+1):
#     s,b = list(map(int,input().split()))
#     members.append(Member(s,b,i))
#   members[1:] =sorted(members[1:])
#   for m in members:
#       print(m)
#   ans,res = LIS(members)
#   print (ans)
#   for i in reversed(res):
#     print('{} '.format(i),end = '')


#   #  print('Case {}: maximum height = {}'.format(Case,res))
#   #  Case += 1

# if __name__ == "__main__":
#   main()