def solution(num_list):
    answer = []
    a=0
    b=0
    i=0
    for i in range(i, len(num_list)):
        if num_list[i]%2==0:
            a=a+1
        else:
            b=b+1
    answer.append(a)
    answer.append(b)
    return answer