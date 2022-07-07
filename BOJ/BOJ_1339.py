N = int(input())
decimal = [0] * 27

for _ in range(N):
    tmp = list(map(str, input()))
    for i, k in enumerate(reversed(tmp)):
        decimal[ord(k)-64] += 10**i
decimal.sort(reverse=True)
result = 0
cnt = 9
for k in decimal:
    if k:
        result += k*cnt
        cnt -= 1
    else:
        break
print(result)