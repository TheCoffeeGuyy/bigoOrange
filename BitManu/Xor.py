# public static void main(String[] args) {
#         int t, n;
#         Scanner sc = new Scanner(System.in);
#         t = sc.nextInt();
#         while (t > 0) {
#             t -= 1;
#             n = sc.nextInt();
#             int tmp, res = 0;
#             for (int i = 0; i < n; i++) {
#                 tmp = sc.nextInt();
#                 if (((long)n - i) * (i + 1) % 2 == 1)
#                     res ^= tmp;
#             }
#             System.out.println(res);
#         }
#     }

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    res = 0
    for i in range(n):
        if (n - i) * (i + 1) % 2== 1:
            res ^= arr[i]
    
    print(res)