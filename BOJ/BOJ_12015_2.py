import sys
from bisect import bisect_left

input = sys.stdin.readline

N = int(input()) #수열의 길이
A = list(map(int, input().split())) #수열
lis = [] #부분 수열

for num in A:
    if not lis: # 초기 값 넣어주기
        lis.append(num)
        continue
    if lis[-1] < num: # lis의 마지막(최대값)과 새로운 값 비교
        lis.append(num)
    else:
        index = bisect_left(lis, num)
        lis[index] = num

print(len(lis))