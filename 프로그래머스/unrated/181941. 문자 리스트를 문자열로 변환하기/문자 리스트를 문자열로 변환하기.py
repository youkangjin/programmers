def solution(arr):
    answer=''
    i=0
    j=0
    for i in range(i,len(arr)):
        answer = answer+arr.pop(j)
    
    return answer