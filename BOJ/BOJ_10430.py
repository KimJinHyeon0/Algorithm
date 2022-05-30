A, B, C = map(int, input().split())
result1 = (A+B)%C
result2 = ((A%C)+(B%C))%C
result3 = (A*B)%C
result4 = ((A%C)*(B%C))%C
print(result1, result2, result3, result4, sep=('\n'))