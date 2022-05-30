from copy import deepcopy

# def BFS(arr, cnt):
#     if cnt == 4:
#         asdf
#
#     for i in range(N):
#         for j in range(N):



N = int(input())
nums = []
for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(N):
        if temp[j]:
            nums.append([i, j, temp[j]])
print(nums)
dx_l = [1, 0, -1, 0]
dy_l = [0, 1, 0, -1]

# BFS(table, 0)