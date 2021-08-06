p=input()
while p!='0':
    p=list(map(int, p))
    cnt = 0
    for _ in range(len(p)//2):
        if p[_]==p[-_-1]:
            cnt+=1
        else:
            pass

    if len(p)//2==cnt:
        print('yes')
    else:
        print('no')
    p=input()