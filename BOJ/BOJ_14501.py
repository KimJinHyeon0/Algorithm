N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
result = 0
def dfs(day, money, table):
    global result
    if day == N:
        result = max(result, money)
        print(table)
        return
    dfs(day + 1, money, table) #x일에 일 안하고 내일로 보내기
    if day+data[day][0] <= N: #x일에 있는 일 받고, 그 일 끝난 날로 이동
        dfs(day+data[day][0], money+data[day][1], table + [day])


dfs(0, 0, [])
print(result)