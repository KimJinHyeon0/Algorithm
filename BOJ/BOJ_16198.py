from copy import deepcopy
N = int(input())
marbel_l = list(map(int, input().split()))
result = 0

def bfs(i, m_l, tmp, cnt):
    global result

    cp = deepcopy(m_l)
    tmp += (cp[i-1] * cp[i+1])
    cp.pop(i)
    cnt -= 1

    if cnt == 2:
        result = max(result, tmp)
        return

    for i in range(1, cnt-1):
        bfs(i, cp, tmp, cnt)

for i in range(1, N-1):
    bfs(i, marbel_l, 0, N)

print(result)