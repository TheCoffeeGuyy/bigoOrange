# t = int(input())
# for i in range(t):
#     n, m = map(int, input().split())
#     integer = 0
#     frac = m
#     tempm = m
#     while tempm // n > 0:
#         tempm = tempm // n
#         integer += 1
#     if integer > 0:
#         frac = m - n ** integer
#     buildStr = ''
#     buidFrac = ''
#     for i in range(frac):
#         if i == frac - 1:
#             buildStr += f'({n}<<0)'
#         else:
#             buildStr += f'({n}<<0) + '
#     if integer > 0:
#         buidFrac =  f'({n}<<{integer})'
#         print(buidFrac + ' + '+ buildStr)
#     else:
#         print(buildStr)

print(2 << 2)