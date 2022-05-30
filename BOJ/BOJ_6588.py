import sys
from itertools import combinations

def primeNum(a):
    if a == 1:
        return False
    for i in range(2, a):
        if a%i == 0:
            return False
    return True

data = True
while data:
    data = int(input())
    datas = []
    ans = (0,0)
    for j in range(1, data, 2):
        if primeNum(j) == True:
            datas.append(j)
    for case in combinations(datas,2):
        if sum(case) == data:
            if (ans[1]-ans[0]) < (case[1]-case[0]):
                ans = case
    if ans == (0,0):
        print("Goldbach's conjecture is wrong.")
    else:
        print(data,'=',ans[0],'+',ans[1],sep=' ')
