def solution(num_list):
    answer = 0
    i=0
    a=0
    b=0
    while(i<len(num_list)):
        if i%2==0:
            a+=num_list[i]
            i+=1
        elif i%2==1:
            b+=num_list[i]
            i+=1
    if a>b:
        answer=a
    elif a<b:
        answer=b
    else:
        answer=a
    return answer