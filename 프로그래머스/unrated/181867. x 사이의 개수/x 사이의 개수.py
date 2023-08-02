def solution(myString):
    answer = []
    a=0
    i=0
    b=0
    for i in range(i, len(myString)):
        if myString[i] in "x":
            answer.append(a)
            a=0
        else:
            a=a+1
            if i == len(myString)-1:
                answer.append(a)
        b=len(myString)
    b=len(myString)   
    if myString[b-1] in "x":
        answer.append(0)
    return answer