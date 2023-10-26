def solution(s):
    answer=[]
    a=s.split()
    b=0
    for i, j in enumerate(a):
        if j=="Z":
            answer.pop(-1)
        else:
            answer.append(j)
    for k in answer:
        b+=int(k)
        
    return b