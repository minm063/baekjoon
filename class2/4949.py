while True:
    flag=1
    tmp=[]
    S=input()
    if S=='.':
        break
    
    for _ in S:
        if _=='(' or _=='[':
            tmp.append(_)
        elif _==')':
            if tmp and tmp[-1]=='(':
                tmp.pop()
            else:
                flag=0
                break
        elif _==']':
            if tmp and tmp[-1]=='[':
                tmp.pop()
            else:
                flag=0
                break
    print("yes" if flag and not tmp else "no")