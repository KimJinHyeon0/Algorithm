import sys
from itertools import permutations

input = lambda : sys.stdin.readline()

N = int(input())
weight = sorted(list(map(int, input().split())))
print(weight)
is_valid = [False] * (sum(weight) + 1)
is_valid[0] = True

min = 0

for i in range(len(weight)):
    permut = list(permutations(weight, i))

    for case in permut:
        is_valid[sum(case)] = True


    if min < is_valid.index(False): # 1번째 false
        min = is_valid.index(False)
    else:
        break

print(min)
