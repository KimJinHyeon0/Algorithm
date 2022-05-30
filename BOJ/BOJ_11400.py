v, e = map(int, input().split())
edges = [[] for i in range (v+1)]
for _ in range(e):
    s, d = map(int, input().split())
    edges[s].append(d)
    edges[d].append(s)

print(v, e, edges)