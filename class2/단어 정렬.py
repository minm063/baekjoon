N=int(input())
str_list=[]
while N:
    s=input()
    str_list.append(s)
    N-=1

str_list=list(set(str_list))
str_list.sort()
str_list=sorted(str_list, key=lambda str_list: len(str_list))

print('\n'.join(str_list))