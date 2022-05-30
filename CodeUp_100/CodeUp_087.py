data = int(input())
tot = 0
for i in range(0, 1000000):
    tot +=i
    if data <= tot:
        print(tot)
        break
