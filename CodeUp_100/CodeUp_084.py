r, g, b = map(int, input().split())
count = 0
for r_i in range(0, r):
    for g_i in range(0, g):
        for b_i in range(0, b):
            count = count + 1
            print (r_i, g_i, b_i, sep=' ')
print(count)
