N = int(input())
m_l = list(list(map(int, input().split())) for _ in range(N))
dp = [[0] * N for i in range(N)]

for i in range(1, N):
    for j in range(N-i):
        x = j + i
        dp[j][x] = 2**32
        for k in range(j, x):
            dp[j][x] = min(dp[j][x], dp[j][k] + dp[k+1][x] + m_l[j][0] * m_l[k][1] * m_l[x][1])

print(dp[0][N-1])