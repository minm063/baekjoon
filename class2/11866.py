# 요세푸스 문제 0
from collections import deque

N, K = map(int, input().split(' '))
queue = deque(list(range(1,N+1)))
answer=[]

# JP.remove(cnt)
# while len(JP)>1:
#     if cnt>=N:
#         cnt = cnt + K - N
#         JP.remove(cnt)
#     else:
#         cnt += K
#         JP.remove(cnt)

while len(queue):
    for _ in range(K):
        queue.append(str(queue.popleft()))
    answer.append(queue.pop())
print('<%s>' % ', '.join(answer))