n, k = map(int, input().split())
dp = [0 for _ in range(k+1)]
dp[0] = 1
for i in range(n):
    coin = int(input())
    for k in range(1, k+1):
        if k >= coin:
            dp[k] += dp[k-coin]

print(dp[k])

