from collections import deque
import sys
input = lambda : sys.stdin.readline()

N = int(input())
apple = [list(map(int, input().split())) for _ in range(int(input()))]
turn = deque((list(map(str, input().split()))) for _ in range(int(input())))

snake = deque([[1, 1]])
directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
n = 0
time = 0

while (0 < snake[-1][0] < N+1) and (0 < snake[-1][1] < N+1):
    time += 1
    if turn and time == int(turn[0][0])+1:
        k = turn.popleft()
        if k[1] == 'D':
            n = (n+1) % 4
        else:
            n = (n+3) % 4

    temp = directions[n]
    next_step = list(x+y for x, y in zip(snake[-1], temp))
    if next_step in snake:
        break
    snake.append(next_step) #head move
    if next_step in apple:
        apple.remove(next_step)
    else:
        snake.popleft() #tail off

print(time)