def primeNum(a):

    i=3
    while i*i <=a:
        if a%i==0 :
            return False
        else:
            i+=2
    return True

def goldBach(n):

    for i in range(3, n, 2):
        if primeNum(i) and primeNum(n-i):
            return i
    return -1

data = True
while data:
    data = int(input())
    gold = goldBach(data)
    if gold == -1:
        print("Goldbach's conjecture is wrong.")
    else:
        print('{} = {} + {}'.format(data,gold,data-gold))