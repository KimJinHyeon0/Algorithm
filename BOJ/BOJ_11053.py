N = int(input())
A = list(map(int, input().split()))
dp = [[[i, 1]] * N for i in range(N)]

print(dp, '\n\n')

for i in range(N):
    for j in range(i+1, N):
        if A[j] > A[dp[i][j-1][0]]:
            dp[i][j:] = [[j, dp[i][j-1][1] + 1]] * (N - j)

result = 0
for i in range(N):
    result = max(dp[i][-1][1], result)
print(dp)
print(result)