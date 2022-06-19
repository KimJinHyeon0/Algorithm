N = int(input())
dp = [[0, 0] for _ in range(N+1)]
dp[1] = [0, 1]
if N > 1:
    for i in range(2, N+1):
        dp[i][0] = sum(dp[i-1])
        dp[i][1] = dp[i-1][0]
print(dp)
print(sum(dp[N]))
