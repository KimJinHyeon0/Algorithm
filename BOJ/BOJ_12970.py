n , k = map(int,input().split())
s = 'B' * n
s = list(s)
def check(word):
    cnt = 0
    for i in range(n-1):
        if word[i] == 'A':
            for j in range(i+1, n):
                if word[j] == 'B':
                    cnt += 1
    return cnt

for i in range(n):
    s[i] = 'A'
    if check(s) == k:
        break
    elif check(s) > k:
        s[i] = 'B'

result = "".join(s)
if result== 'B'*n or result== 'A'*n:
    if k == 0:
        print(result)
    else:
        print(-1)
else:
    print(result)
