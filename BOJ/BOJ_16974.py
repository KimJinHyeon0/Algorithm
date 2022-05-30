N, X = map(int, input().split())

dp = [[1] for _ in range(N+1)]
for i in range(1, N+1):
    dp[i] = [0] + dp[i-1] + [1] + dp[i-1] + [0]
print(sum(dp[N][:X]))