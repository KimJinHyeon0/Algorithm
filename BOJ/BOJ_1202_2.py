# 최대힙을 구현하기 위해 heapq 모듈 import
import sys, heapq
n, k = map(int,sys.stdin.readline().split())
gem_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# temp : 최대힙을 만들어 주기 위해 빈 리스트 생성
temp = []
ans = 0

# 가방 입력
for i in range(k):
    a = int(sys.stdin.readline())
    # [가방의 무게, 가방의 가치] : 가방은 보석들과 구분 되기 위해 보석의 최대 가치보다 더 크게
    # 설정하거나 -1로 설정함으로서 해당 원소가 가방임을 알려준다
    gem_list.append([a,1000002])

# 무게 순 정렬
gem_list.sort()

for i in gem_list:
    # 가방이 아니라면 보석이므로 최대 힙에 담는다
    if i[1] != 1000002:
        # heapq는 최소힙이므로 넣을 때 -1을 곱해 최대힙으로 변형시킨다
        # 자세한 설명은 heapq 모듈을 검색하는것을 추천한다
        heapq.heappush(temp, (-1 * i[1], i[1]))
    else:
        # 만일 가방의 갯수가 보석보다 많다면 pop할 수 없으므로 예외처리
        try:
            ans += heapq.heappop(temp)[1]
        except:
            pass
print(ans)


