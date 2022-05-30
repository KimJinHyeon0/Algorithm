n = int(input())
data = list(map(int, input().split()))
count = list()
for i in range(0,23):
    count.append(data.count(i+1))
for i in range(0,23):
    print(count[i],end=' ')
