import sys

input = lambda : sys.stdin.readline()

#N, K
N, K = map(int, input().split())

#jew 정의
jew = [list(map(int, input().split())) for _ in range(N)]

#bag 정의
bag = [int(input())for _ in range(K)]

#main
bag.sort() # 작은 무게의 가방부터 검사
heap = []
tot = 0 # 보석 가격의 총합
for i in range(K):
    for j in range(N):
        if jew[j][0] <= bag[i]:
            if temp[1] < jew[j][1]:
                temp[0], temp[1] = j, jew[j][1]
    jew[temp[0]] = [0,0] #가방에 넣은 보석 정보 0,0으로 초기화
    tot += temp[1]
    temp = [0,0] #temp 초기화
print(tot)
