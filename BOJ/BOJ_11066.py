for _ in range(int(input())):
    result = 0
    K = int(input())
    data = list(map(int, input().split()))
    for i in range(K-1):
        data.sort()
        A = data.pop(0)
        result += A+data[0]
        data[0] += A
        print(data)
    print(result)