N=int(input())
member=[]
while N:
    member_age, member_name = map(str, input().split())
    member_age = int(member_age)
    member.append((member_age, member_name))
    N-=1

member=sorted(member, key=lambda x:x[0])
for m in member:
    print(m[0], m[1])