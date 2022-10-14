# 주사위 굴리기 2

def dfs(x, y, t):
    global score
    score += 1

    visited[x][y] = True

    for i in range(4):
        nx, ny = x + dir_l[i][0], y + dir_l[i][1]
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and table[nx][ny] == t:
            dfs(nx, ny, t)


class Dice:
    def __init__(self):
        self.one = 1
        self.two = 2
        self.three = 3
        self.four = 4
        self.five = 5
        self.six = 6

        self.x = 0
        self.y = 0
        self.d = 0

        self.point = 0

    def change(self):
        if self.d == 0:
            self.four, self.one, self.three, self.six = self.six, self.four, self.one, self.three

        elif self.d == 1:
            self.two, self.one, self.five, self.six = self.six, self.two, self.one, self.five

        elif self.d == 2:
            self.four, self.one, self.three, self.six = self.one, self.three, self.six, self.four

        elif self.d == 3:
            self.two, self.one, self.five, self.six = self.one, self.five, self.six, self.two

    def step(self):
        nx, ny = self.x + dir_l[self.d][0], self.y + dir_l[self.d][1]
        if 0 <= nx < N and 0 <= ny < M:
            self.x = nx
            self.y = ny

            self.change()

        else:
            self.d = (self.d + 2) % 4
            self.step()

    def get_point(self):
        b = table[self.x][self.y]
        dfs(self.x, self.y, b)
        self.point += (b * score)

    def next(self):
        a = self.six
        b = table[self.x][self.y]

        if a > b:
            self.d = (self.d + 1) % 4
        elif a < b:
            self.d = (self.d - 1) % 4

    def move(self):
        self.step()
        self.get_point()
        self.next()


N, M, K = map(int, input().split())
table = list(list(map(int, input().split())) for _ in range(N))
dir_l = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # 동 남 서 북
dice = Dice()
for _ in range(K):
    visited = [[False] * M for _ in range(N)]
    score = 0
    dice.move()
print(dice.point)
# print(f'x, y = {dice.x, dice.y} | bottom : {dice.six} | direction : {dice.d}, score : {score}')
# print('_', dice.two)
# print(dice.four, dice.one, dice.three)
# print('_', dice.five)
# print('_', dice.six)


'''
move
    if not in table -> backward
get point
compare A, B -> choose direction
new direction

get point : 
    
'''