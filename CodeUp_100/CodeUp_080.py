data = int(input())
tot = 0
for i in range(1,100):
    tot = tot + i
    if data <= tot:
        print(i)
        break
