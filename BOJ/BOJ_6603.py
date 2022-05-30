from itertools import combinations

def cal(data):
    combi = list(combinations(data, 6))
    for case in combi:
        print(' '.join(case))
    print()

while True:
    t = list(map(str, input().split()))
    if len(t) == 1:
        break
    k = int(t[0])
    data = t[1:]
    cal(data)