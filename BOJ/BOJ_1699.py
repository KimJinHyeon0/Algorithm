N = int(input())
dp = [0 for i in range(N + 1)]
sqrt = [i * i for i in range(1, N)]
for i in range(1, N + 1):
    tmp = []
    for j in sqrt:
        if j > i:
            break
        tmp.append(dp[i - j])
    print(i, tmp)
    dp[i] = min(tmp) + 1

print(dp)