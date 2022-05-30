def dfs(state, k, result, arr):
    global maxi, mini
    state += 1
    if k == 0:
        result += num[state]
    elif k == 1:
        result -= num[state]
    elif k == 2:
        result *= num[state]
    else:
        if result >= 0:
            result /= num[state]
        else:
            result = -(result*(-1)/num[state])
    arr[k] -= 1

    if state == N-1:
        if result >= maxi:
            maxi = result
        if result <= mini:
            mini = result
        return

    for i in range(4):
        if arr[k] != 0:
            dfs(state+1, i, result, arr)

N = int(input())
num = list(map(int, input().split()))
ele = list(map(int, input().split()))
mini = 1e10
maxi = -1e10
for j in range(4):
    if ele[j] != 0:
        dfs(0, j, num[0], ele)
print(mini)
print(maxi)