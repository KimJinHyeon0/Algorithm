Max = 1000000
prime = [False for i in range(Max+1)]

for i in range(2, Max+1):
    if i*i > Max:
        break
    if prime[i] is False:
        for j in range(i*i, Max+1, i):
            prime[j] = True

data = True
while data:
    data = int(input())
    ans = [0,0]
    for i in range(2, Max+1):
        if prime[i] == False:
            j = data - i
            if prime[j] == False:
                if ans[1] < j:
                    ans = [i,j]
    if ans == [0, 0]:
        print("Goldbach's conjecture is wrong.")
    else:
        print(data, '=', ans[0], '+', ans[1], sep=' ')