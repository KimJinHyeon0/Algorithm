def gcd(a,b):
    if a<b:
        a, b = b, a
    while b != 0:
        a, b = b, a%b
    return a

def prime(a):
    if a <2:
        return False
    for i in range(2, a):
        if gcd(i,a) == 1:
            return True
        else:
            return False

N = int(input())
data = list(map(int,input().split()))

for i in range(N):
    data[i] = prime(data[i])
print(data.count(True))
