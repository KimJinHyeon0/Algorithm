import sys
from collections import deque
input = lambda: sys.stdin.readline()

S = int(input())
record = [0] * (S+1)
clipboard = 0
length = 1
cnt = 0

def operation(oper):
    global length, cnt, is_valid, clipboard
    #delete
    if oper == 1:
        next_length = length - 1
        cnt =+ 1
        print('delete')
        return next_length

    #paste
    if oper == 2 and not clipboard:
        next_length = length + clipboard
        cnt += 1
        print('paste')
        return next_length

    #copy
    if oper == 3:
        clipboard = length
        cnt += 1
        print('copy')
        return length


queue = deque()
queue.append(3)

while queue:
    oper = queue.popleft()
    length = operation(oper)

    for i in range(1, 4):
        next_length = operation(i)
        print('next_length', next_length)
        if next_length > S or next_length < 0:
            continue
        if not record[next_length]:
            record[next_length] = cnt
            queue.append(i)
    print(queue)
    print(record)

print('--------')
print(record)
print(record[S])