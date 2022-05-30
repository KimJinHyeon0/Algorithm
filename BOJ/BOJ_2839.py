n = int(input())
five = n//5
left = n-five*5
three = left//3
check = left%3
if check:
    print(-1)
else:
    print(five+three)
