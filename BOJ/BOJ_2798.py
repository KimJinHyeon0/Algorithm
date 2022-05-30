N, M = map(int, input().split())
card = list(map(int, input().split()))
tot_list = []
tot = int()
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            tot = card[i]+card[j]+card[k]
            if tot <= M:
                tot_list.append(tot)
tot_list.sort()
print(tot_list[-1])
