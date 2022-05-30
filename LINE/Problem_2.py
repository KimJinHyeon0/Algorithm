n = 5
times = [2, 4, 5]
def solution(n, times):
    dp = [[1e10] * len(times) for _ in range(n)]
    dp[0] = [0] * len(times)

    for i in range(1, n):
        for j, time in enumerate(times):
            if i >= j+1:
                print(i, j)
                dp[i][j] = min(dp[i- j-1]) + times[j]
    return min(dp[n-1])

solution(n, times)