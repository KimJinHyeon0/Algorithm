n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
S = 0
-
for a, b in zip(sorted(A), sorted(B, reverse=True)):
    S += a*b

print(S)