def dfs(i, cnt, nodes):
    global result
    if cnt == i:
        temp = 0
        for x in nodes:
            temp += A[x]
        if temp == S:
            result += 1
        return

    for k in range(N):
        if not visited[k]:
            visited[k] = True
            dfs(i, cnt+1, nodes+[k])
            visited[k] = False

N, S = map(int, input().split())
A = list(map(int, input().split()))

result = 0

for i in range(1, N+1):
    visited = [False] * N
    dfs(i, 0, [])
print(result)

dfs