def gcd(a,b):
    if a<b:
        a, b = b, a
    while b != 0:
        a, b = b, a%b
    return a

t = int(input())

for i in range(t):
    tot = 0
    data = []
    data = list(map(int, input().split()))
    for j in range(1, len(data)-1):
        for k in range(j+1, len(data)):
            tot += gcd(data[j],data[k])
    print(tot)
