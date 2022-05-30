 T = int(input())
for t in range(T):
    result = 0
    N = int(input())
    core_l = []
    for i in range(N):
        tmp = list(map(int, input().split()))
        for j, k in enumerate(tmp):
            if k == 1:
                core_l.append([i, j])

    print(core_l)
    print('#{t+1} {result}')
