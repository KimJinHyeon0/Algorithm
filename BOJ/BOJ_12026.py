N = int(input())
data = list(map(str, input()))
MAX = 1e6 +1
dp = [MAX] * N

def get_prev(x):
    if x == 'B':
        return 'J'
    elif x == 'O':
        return 'B'
    else:
        return 'O'

dp[0] = 0
for i in range(1, N):
    prev = get_prev(data[i])
    for j in range(i):
        if data[j] == prev:
            dp[i] = min(dp[i], dp[j] + (i-j)**2)

if dp[-1] == MAX:
    print(-1)
else:
    print(dp[-1])