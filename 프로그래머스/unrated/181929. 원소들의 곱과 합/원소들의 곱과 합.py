def solution(num_list):
    i=0
    a=1
    j=0
    b=0
    for i in range(i,len(num_list)):
        a=num_list[i]*a
    
    for j in range(j,len(num_list)):
        b=num_list[j]+b
        
    if a<b*b:
        return 1
    elif a>b*b:
        return 0