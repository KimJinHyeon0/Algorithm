import sys
import math

input = lambda : sys.stdin.readline()

x, y = map(int, input().split())

# z = int((y/x)*100)
z = y * 100 // x

if z >= 99:
    print(-1)
else:
    a = ((x * z) + x - (100 * y)) / (99 - z)
    print(math.ceil(a))