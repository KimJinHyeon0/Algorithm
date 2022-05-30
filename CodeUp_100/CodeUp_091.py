a, m, d, n = map(int, input().split())
num = a
if n>1:
    for i in range(1, n):
        num = num*m+d   
print(num)

