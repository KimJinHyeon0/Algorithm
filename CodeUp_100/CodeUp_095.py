n = int(input())
data = list(map(int, input().split()))
count = []
for i in range(0,23):
    count.append(data.count(i+1))
for t in range(0,23):
    if count[t] != 0:
        print(t+1)
        break
