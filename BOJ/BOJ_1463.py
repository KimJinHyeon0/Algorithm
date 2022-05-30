N = int(input())
dp = [1e6] * (N+1)
dp[1] = 0
for i in range(1, N+1):
    if i*3 <= N:
        dp[i*3] = min(dp[i*3], dp[i] + 1)
    if i*2 <= N:
        dp[i*2] = min(dp[i*2], dp[i] + 1)
    if i+1 <= N:
        dp[i+1] = min(dp[i+1], dp[i] + 1)
print(dp[N])