def check():
    for i in range(N):
        y = i
        for x in range(H):
            y += table[x][y]
        if y != i:
            return False
    return True

def BFS(cnt):
    global result

    if check():
        result = min(result, cnt)
        return

    elif cnt == 3 or result < cnt:
        return

    for i in range(H):
        for j in range(N-1):
            if table[i][j:j+2] == [0, 0]:
                table[i][j:j+2] = [1, -1]
                BFS(cnt+1)
                table[i][j:j + 2] = [0, 0]

N, M, H = map(int, input().split())

table = [[0 for _ in range(N)] for _ in range(H)]
for _ in range(M):
    x, y = map(int, input().split())
    table[x-1][y-1:y+1] = [1, -1]
result = 5
BFS(0)

print(result if result < 5 else -1)