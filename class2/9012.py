N=int(input())
while N:
    flag=1
    s=input()
    tmp=[]
    for _ in s:
        if _=='(':
            tmp.append(_)
        elif _==')':
            if not tmp:
                flag=0
                break
            if tmp[-1]=='(' and tmp:
                tmp.pop()
            else:
                flag=0
                break
    print("YES" if flag==1 and not tmp else "NO")
    N-=1