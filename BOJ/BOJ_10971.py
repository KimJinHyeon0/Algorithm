import sys
from itertools import combinations, permutations

n = int(sys.stdin.readline())
w = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
test = [i for i in range(n)]
ans = 12000000

for data in permutations(test, n):
    total = 0
    for j in range(0, n):
        total += w[data[j-1]][data[j]]
    if ans > total:
        ans = total
print(ans)

