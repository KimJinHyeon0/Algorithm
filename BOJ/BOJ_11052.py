N = int(input())
P = [0] + list(map(int, input().split()))
dp = [0] * (N+1)
dp[:N] = P
for i in range(2, N+1):
    for j in range(1, i):
        dp[i] = max(dp[i-j] + P[j], dp[i])
print(dp[N])