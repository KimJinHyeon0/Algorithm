n, k = map(int, input().split())
coins = []
dp = [10002 for _ in range(k+1)]
for _ in range(n):
    coin = int(input())
    if coin <= k:
        coins.append(coin)
        dp[coin] = 1
for i in range(k+1):
    for coin in coins:
        print(dp)
        if i>= coin:
            dp[i] = min(dp[i], dp[i-coin]+1) # 10002,.

print(dp[k])