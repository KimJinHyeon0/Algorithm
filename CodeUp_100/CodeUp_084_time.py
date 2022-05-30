import time

hmt = int(input("how many time?"))
tot_time = 0
r, g, b = map(int, input('r,g,b=').split())
for i in range(0, hmt+1):
    start = time.time()
    count = 0
    for r_i in range(0, r):
        for g_i in range(0, g):
            for b_i in range(0, b):
                count = count + 1
                print (r_i, g_i, b_i, sep=' ')
    print(count)
    print(time.time()-start)
    tot_time = tot_time + (time.time()-start)
print("avg_time =",tot_time/hmt,"s")
