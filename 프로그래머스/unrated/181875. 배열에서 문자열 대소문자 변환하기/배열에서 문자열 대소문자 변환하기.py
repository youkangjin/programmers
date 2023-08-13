def solution(strArr):
    answer = []
    i=0
    a=""
    b=""
    for i in range(i, len(strArr)):
        if i%2==0:
            a=strArr[i]
            b=a.lower()
            answer.append(b)
        else:
            a=strArr[i]
            b=a.upper()
            answer.append(b)
    return answer