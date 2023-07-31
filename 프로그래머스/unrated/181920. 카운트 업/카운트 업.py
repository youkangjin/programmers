def solution(start, end):
    answer = []
    i=0
    for i in range(i,end-start+1):
        answer.append(start)
        start=start+1
    return answer