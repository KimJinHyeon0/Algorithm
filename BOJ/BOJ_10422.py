import sys
input = lambda: sys.stdin.readline()

d = [0]*2501 # 괄호쌍의 갯수이므로 5000//2 -> 2501
d[0] = 1

def cat(x): #catalian number
    if d[x] != 0:
        return d[x]
    else:
        for i in range(x):
            d[x] += d[i]*d[x-i-1]
            d[x] = d[x] % 1000000007 # 곱의 나머지 == 나머지의 곱
        return d[x]

for j in range(2501): #2501개 쌍의 괄호에 대해 카탈린 수 적용
    cat(j)

T = int(input())
for _ in range(T):
    L = int(input())
    if L == 1:
        result = int(0)
    elif L % 2 == 1:
        result = int(0)
    else:
        result = int(cat(L//2)) # L = 문자열의 총 길이. L//2 = 문자열 내 괄호쌍의 수
    print(result)