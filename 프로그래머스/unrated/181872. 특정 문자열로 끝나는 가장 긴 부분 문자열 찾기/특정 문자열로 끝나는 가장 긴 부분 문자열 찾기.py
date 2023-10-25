def solution(myString, pat):
    answer = ''
    a=0
    for i in range(len(myString)):
        if pat[-1]==myString[i]:
            a=i
        
    answer=myString[:a+1]
    return answer