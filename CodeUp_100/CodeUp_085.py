audio = list(map(int, input().split()))
size = 1
for i in audio:
    size = size*i
size = size / 8 ##bit -> byte
size = size / 1024 ##byte -> Kb
size = size / 1024 ##Kb -> Mb
print("%.1f MB" %size) 
