import heapq
n, k = map(int, input().split())
jew_l = [list(map(int, input().split())) for _ in range(n)]

tmp = []
ans = 0

for i in range(k):
    a = int(input())
    jew_l.append([a, 1000002])

jew_l.sort()
for i in jew_l:
    if i[1] != 1000002:
        heapq.heappush(tmp, (-1 * i[1], i[1]))
    else:
        try:
            ans += heapq.heappop(tmp)[1]
        except:
            pass
print(ans)


