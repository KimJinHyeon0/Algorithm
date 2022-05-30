N = int(input())
num = []
for i in range(0,N+1):
    num.append(i)

count = 0
A = 0
ans = []
while count < N:
    B = int(input())
    if A<B:
        for i in range(int(num.index(B))-int(num.index(A))+1):
            ans.append('+')
    ans.append('-')
    del num[num.index(B)]    
    A = B
    count += 1

print(ans,sep='\n')

