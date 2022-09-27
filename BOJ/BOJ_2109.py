n = int(input())
if n == 0:
    print(0)
    exit()

data = list(list(map(int, input().split())) for _ in range(n))
data.sort(reverse=True)
print(data)
max_d = max(data[i][1] for i in range(n)) + 1
visited = [False] * max_d
result = 0

for pay, day in data:
    for i in range(day):
        if not visited[i]:
            visited[i] = True
            result += pay
            break

print(result)