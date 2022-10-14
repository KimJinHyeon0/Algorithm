# 주사위 굴리기

def show(x):
    for row in x:
        print(*row)

class Dice():
    def __init__(self, x, y):
        self.coor_x = x
        self.coor_y = y

        self.one = 0
        self.two = 0
        self.three = 0
        self.four = 0
        self.five = 0
        self.six = 0


    def move(self, d):
        if d == 1:
            self.four, self.one, self.three, self.six = self.six, self.four, self.one, self.three
        elif d == 2:
            self.four, self.one, self.three, self.six = self.one, self.three, self.six, self.four
        elif d == 3:
            self.two, self.one, self.five, self.six = self.one, self.five, self.six, self.two
        elif d == 4:
            self.two, self.one, self.five, self.six = self.six, self.two, self.one, self.five


    def roll(self, d):
        nx, ny = self.coor_x + dir_l[d][0], self.coor_y + dir_l[d][1]
        if 0 <= nx < N and 0 <= ny < M:
            self.coor_x, self.coor_y = nx, ny
            self.move(d)

            if table[nx][ny] == 0:
                table[nx][ny] = self.six
            else:
                self.six, table[nx][ny] = table[nx][ny], 0
            # print(f'x, y = {self.coor_x, self.coor_y}')
            print(self.one)


N, M, x, y, K = map(int, input().split())
table = list(list(map(int, input().split())) for _ in range(N))
move_l = list(map(int, input().split()))
dir_l = [[], [0, 1], [0, -1], [-1, 0], [1, 0]]
dice = Dice(x, y)
for d in move_l:
    dice.roll(d)
