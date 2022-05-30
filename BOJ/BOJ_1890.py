import sys
input = lambda: sys.stdin.readline()

n = int(input())
data = [[int(x) for x in input().split()] for y in range(n)]
data[n-1][n-1]  = 1
cnt = 0
dp = []
if data[0][0] < n:
    dp += [data[0][0],0], [0,data[0][0]]
len_dp = len(dp) # 2
while len_dp:
    for m in range(len(dp)):
        if dp[m][0]+data[dp[m][0]][dp[m][1]] < n: #아랫쪽으로
            dp += [[dp[m][0]+data[dp[m][0]][dp[m][1]],dp[m][1]]]
        if dp[m][1]+data[dp[m][0]][dp[m][1]] < n: # 오른쪽으로
            dp += [[dp[m][0],dp[m][1]+data[dp[m][0]][dp[m][1]]]]
    del dp[:len_dp]
    cnt += dp.count([n-1, n-1])
    len_dp = len(dp)
print(cnt)