# T=int(input())
# cnt=1
# while cnt<=T:
#     hotel=list(map(int, input().split()))
#     H, W, N = hotel

#     n=1
#     tmp=N
#     while tmp-H>H:
#         tmp-=H
#         n+=1
#     print(H, W, N, n)
#     if n<10:
#         print(str(N-H*n)+'0'+str(n+1))
#     else:
#         print(str(N-H*n)+str(n+1))
#     cnt+=1

T=int(input())
cnt=1
while cnt<=T:
    H,W,N = list(map(int, input().split()))

    a, b=N%H, N//H+1
    if a==0:
        a=H
        b-=1
    print(a*100+b)