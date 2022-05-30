def dfs(idx, sum):
    global result
    if idx == N:
        return
    sum += data[idx]
    if sum == S:
        result += 1
    dfs(idx+1, sum - data[idx])
    dfs(idx+1, sum)

N, S = map(int, input().split())
data = list(map(int, input().split()))
result = 0
dfs(0, 0)
print(result)


