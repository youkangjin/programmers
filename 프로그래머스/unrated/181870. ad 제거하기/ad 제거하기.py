def solution(strArr):
    answer = []
    i=0
    for i in range(i, len(strArr)):
        if "ad" in strArr[i]:
            i=i+1
        else:
            answer.append(strArr[i])
            i=i+1
    return answer