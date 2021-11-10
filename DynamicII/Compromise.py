import sys
sys.setrecursionlimit(100000000)
def LCS(text1, text2, m, n):
    if m == 0 or n == 0:
        dp[m][n] = 0
        return dp[m][n]
    if dp[m][n] != -1:
        return dp[m][n]
    if text1[m-1] == text2[n-2]:
        dp[m][n] = 1 + LCS(text1, text2, m - 1, n-1)
        return dp[m][n]
    else:
        dp[m][n] = max(LCS(text1, text2, m - 1, n), LCS(text1, text2, m, n-1))
        return dp[m][n]

def printPath(text1, text2, m, n):
    lengthLCS = dp[m][n]
    result = [''] * lengthLCS
    i = m
    j = n
    while i > 0 and j > 0:
        if text1[i - 1] == text2[j-1] :
            result[lengthLCS - 1] = text1[i - 1]
            i -=1 
            j -=1 
            lengthLCS -=1
        elif dp[i-1][j] > dp[i][j-1]:
            i -=1
        else:
            j -=1
    print(result)
    return ' '.join(result)

text1 = '1234567890'
dp = [[-1] * 102 for i in range(102)]
text2 = '13135789340'
print(LCS(text1, text2, len(text1), len(text2)))
print(printPath(text1, text2,len(text1), len(text2)))

# while True:
#     try:
#         dp = [[-1] * 102 for i in range(102)]
#         text1 = []
#         while True:
#             line = input().split()
#             if  line[0] == '#':
#                 break
#             text1.extend(line)
#         text2 = []
#         while True:
#             line = input().split()
#             if  line[0] == '#':
#                 break
#             text2.extend(line)
#         # print(text2)
#         # print(text1)
        
#         print(LCS(text1, text2, len(text1), len(text2)))
#         print(printPath(text1, text2,len(text1), len(text2)))
#     except EOFError:
#         exit()
