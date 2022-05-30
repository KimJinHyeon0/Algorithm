import sys

input = lambda : sys.stdin.readline()

N, K = map(int, input().split())

medal = [list(map(int, input().split())) for _ in range(N)]
country = sorted(medal)[K-1]
medal.sort(key = lambda x: (x[1], x[2], x[3]), reverse=True)
print(medal.index(country))