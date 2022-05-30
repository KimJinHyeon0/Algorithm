M, S = map(int, input().split())
fish_l = list(list(map(int, input().split())) for _ in range(M))
shark = list(map(int, input().split()))
dir_l = [[0, 0], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]

print(M, S)
print(fish_l)
print(shark)