a, b = map(int, input().split())

table = list(list(map(int, input().split())) for _ in range(a))
print(table)
table2 = list(map(list ,zip(*table)))
print(table2)