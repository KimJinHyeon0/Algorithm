a = list(input())
for i in range(5):
    print('['+str(int(a[i])*(10**(len(a)-i-1)))+']', end='\n')
