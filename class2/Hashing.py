'''
    항의 번호에 해당하는 만큼 특정한 숫자를 거듭제곱해서 곱해준 다음 더한다
'''
L=input()
s=input()
r, M, answer = 31, 1234567891, 0
s_dic={}
for _ in range(1,27):
    s_dic[chr(_+96)]=_

for idx, _ in enumerate(s):
    answer+=s_dic[_]*(r**idx)
print(answer%M)