def primeList(k):
    c = [True]*k
    c[:1] = [False]*2
    for i in range(2, int(k**0.5)+1):
        if c[i] == True:
            for j in range(i*2, k+1, i):
                c[j] = False
    return c


N = int(input())
pl = primeList(N)
print(N, pl)
print(pl[N])
111111111111111