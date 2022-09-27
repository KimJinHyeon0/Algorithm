N, K = map(int, input().split())
if K < 6:
    print(0)
    exit()

alpha = [False] * 26
for i in 'antatica':
    alpha[ord(i)-97] = True

result = 0
# word2alpha = [[] for _ in range(N)]
for i in range(N):
    word = input().lstrip('anta').rstrip('tica')
    word2alpha = set(map(lambda x: ord(x)-97, word))
    print(word2alpha)
