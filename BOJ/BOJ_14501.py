N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
result = 0
def dfs(day, money, table):
    global result
    if day == N:
        result = max(result, money)
        return
    dfs(day + 1, money, table)
    if day+data[day][0] <= N:
        dfs(day+data[day][0], money+data[day][1], table + [day])


dfs(0, 0, [])
print(result)