def solution(n, numlist):
    answer = []
    i=0
    for i in range(i, len(numlist)):
        if numlist[i]%n==0:
            answer.append(numlist[i])
    return answer