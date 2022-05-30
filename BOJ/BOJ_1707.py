import sys

def makeAdj(v,e): #adj[]생성 함수
    adj = [[] for _ in range(v + 1)]
    for j in range(e):
        x,y = map(int, sys.stdin.readline().split(' '))
        adj[x].append(y)
        adj[y].append(x)
    return adj


def dfs(v,cnt):
    global result
    visited[v] = cnt
    for c in adj[v]:
        if not(visited[c]):
            dfs(c,cnt+1)
        else:
            if visited[c]%2 == cnt%2:
                result = 'NO'
                return

k = int(sys.stdin.readline()) # case 수 입력
for i in range(k):
    v, e = map(int, sys.stdin.readline().split(' ')) #v,e 입력
    visited = [False] * (v+1) # v+1개의 False값을 가진 visited[] 생성
    visited[0] = 1 #미사용 0번째 값 1로 초기화
    result = 'YES' # 기본 temp 'YES'로 초기화
    adj = makeAdj(v,e)
    dfs(1,cnt=1)
    if visited.count(False):
        result = 'NO'
    print(result,sep='\n')

