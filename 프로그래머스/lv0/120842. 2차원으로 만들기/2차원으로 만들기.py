def solution(num_list, n):
    answer = []
    a=[]
    for i in range(len(num_list)):
        if (i+1)%n==0:
            a.append(num_list[i])
            answer.append(a)
            a=[]
        else:
            a.append(num_list[i])
            
    return answer