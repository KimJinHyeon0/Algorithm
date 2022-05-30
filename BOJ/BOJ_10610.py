import sys
input = lambda : sys.stdin.readline()

N = input().rstrip('\n')
N_len = len(N) # 자릿수 저장
N_list = []
is_valid = 0

for i in range(N_len):
    T = int(N[i])
    N_list.append(T)
    if T == 0:
        is_valid = 1

N_list.sort(reverse=True) #역순으로 sort

#10의 배수인 수이면서 3의 배수인지 검사
if is_valid:
    if sum(N_list) % 3 == 0:
        dec = 10 ** (N_len - 1)
        Num = 0
        for i in range(N_len):
            Num += N_list[i] * dec
            dec //= 10
        print(Num)
    else:
        print('-1')
else:
    print('-1')
