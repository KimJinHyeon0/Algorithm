n = int(input())
ine_sing = list(map(str,input().split()))

visited = [0]*10

def check(i,j,k):
    if k == '<':
        return i<j
    else:
        return i>j

def solve(idx,s):
    global MAX,MIN

    if(idx==n+1):
        if(len(MIN)==0):
            MIN = s
        else:
            MAX = s
        return
    for i in range(10):
        if(visited[i]==0):
            if(idx==0 or check(s[-1],str(i),ine_sing[idx-1])):
                visited[i]=True
                solve(idx+1,s+str(i))
                visited[i]=False

MAX, MIN = "", ""
solve(0 , "")
print(MAX)
print(MIN)