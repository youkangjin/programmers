def solution(num_list):
    i=0
    b=""
    c=""
    for i in range(i,len(num_list)):
        if num_list[i]%2==1:
            a=num_list[i]
            b=str(b)+str(a)
        elif num_list[i]%2==0:
            d=num_list[i]
            c=str(c)+str(d)
        i=i+1
    return int(b)+int(c)