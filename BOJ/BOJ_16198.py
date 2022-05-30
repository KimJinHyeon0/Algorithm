N = int(input())
weights = list(map(int, input().split()))

maximum = 0

def dfs( total, arr):
    global maximum

    if len(arr) == N-2:
        maximum = max(total, maximum)
        return

    for i in range(1, len(arr)-1):

        total += (temp[i-1] * temp[i+1])
        del temp[i]
        dfs(total, temp)

dfs(1, 0, weights)
print(maximum)

n = int(input())
data = list(map(int, input().split()))
