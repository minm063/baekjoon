T=int(input())

while T:
    k=int(input())
    n=int(input())
    p=[[i for i in range(1,n+1)] for j in range(0,k+1)]
    print(p)
    # for i in range(k):
    #     for j in range(1,n):
    #         p[j]+=p[j-1]
    #         print(j, p)
    #     print(k)
    # print(p[-1])
    for i in range(1,k+1):
        tmp=[1]*n
        for j in range(1,n):
            tmp[j-1]=p[i-1][j-1]+p[i][j-2]
            p.append(tmp)
            print(i, j)
    T-=1