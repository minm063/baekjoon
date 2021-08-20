N=int(input())
n, m, answer = 3, 5, 0

while True:
    if N%m==0:
        answer+=(N//5)
        print(answer)
        break
    N-=3
    answer+=1
    if N<0:
        print(-1)
        break