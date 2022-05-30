import sys
from bisect import bisect_left
sys.setrecursionlimit(10**6)
input = lambda : sys.stdin.readline()

def cal(budget, temp):
    temp_budget = budget
    index = bisect_left(temp_budget, temp)
    temp_budget[index:] = [temp] * len(temp_budget[index:])
    if sum(temp_budget) > M:
        cal(budget, temp-1)
    elif M - len(temp_budget[index:]) > sum(temp_budget):
        cal(budget, temp+1)
    else:
        print(temp_budget[-1])

N = int(input())
budget = sorted(list(map(int, input().split())))
M = int(input())

tot = sum(budget)

if M >= tot:
    print(budget[-1])
else:
    temp = (budget[0] + budget[-1])//2
    cal(budget, temp)
