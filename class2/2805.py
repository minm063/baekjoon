# 나무 자르기

N, M=map(int, (input().split()))
height=list(map(int, input().split()))

result=max(height)

while True:
    tmp=0
    for _ in height:
        if _<result:
            pass
        else:
            tmp+=_-result
    if tmp==M:
        break
    result-=1
print(result)