def solution(num_list):
    i=0
    j=len(num_list)
    if num_list[j-1]>num_list[j-2]:
        answer=num_list[j-1]-num_list[j-2]
    else:
        answer=num_list[j-1]*2
    num_list.append(answer)
        
    return num_list