N = int(input())
num = list(map(int, input().split()))
opeartion = list(map(int, input().split()))

maximum = -1e9
minimum = 1e9

def dfs(depth, total, plus, minus, mul, div):
    global maximum, minimum

    if depth == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    if plus:
        dfs(depth + 1, total + num[depth], plus - 1, minus, mul, div)
    if minus:
        dfs(depth + 1, total - num[depth], plus, minus - 1, mul, div)
    if mul:
        dfs(depth + 1, total * num[depth], plus, minus, mul - 1, div)
    if div:
        dfs(depth + 1, int(total / num[depth]), plus, minus, mul, div - 1)


dfs(1, num[0], opeartion[0], opeartion[1], opeartion[2], opeartion[3])
print(maximum)
print(minimum)