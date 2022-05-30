melody = list(map(int, input().split()))

ascending = True
descending = True

for i in range(1,8):
    if melody[i] < melody[i-1]:
        ascending = False
    elif melody[i-1] < melody[i]:
        descending = False
if ascending:
    print ("ascending")
elif descending:
    print("descending")
else:
    print("mixed")
