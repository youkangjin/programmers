def solution(start, end):
    answer = []
    for i in range(end,start+1):
        answer.append(i)
        i=i+1
    answer.reverse()
    return answer