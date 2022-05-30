import sys

input = lambda : sys.stdin.readline()

def test(candidate):

    #서류심사 1등의 면접심사 등수
    B_max = min(candidate)[1]

    #면접심사 1등의 서류심사 등수
    A_max = min(candidate, key = lambda x: (x[1], x))[0]

    winner = list(filter(lambda x: x[1] <= B_max and x[0] <= A_max, candidate))
    print(winner, B_max, A_max)

    loser = list(filter(lambda x: sum(x) > B_max + 1 and sum(x) > A_max + 1 , winner))
    print(len(winner) - len(loser))


T = int(input())

for i in range(T):
    N = int(input())
    candidate = [list(map(int, input().split())) for _ in range(N)]
    test(candidate)
