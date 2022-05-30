import sys
input = lambda : sys.stdin.readline()

N = int(input())
word_list = []
for i in range(N):
    word = str(input()).rstrip('\n')
    word_list.append([len(word), word])
#중복 제거
print('before word_list = ', word_list)
# word_list = list(set(word_list[i][1] for i in range(len(word_list))))
word_list = [list(set(item)) for item in word_list]

print('after word_list = ', word_list)


#정렬
word_list.sort(key = lambda x: (len(x), x))

for i in range(len(word_list)):
    print(word_list[i])