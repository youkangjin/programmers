def solution(n):
    answer = []
    i=1
    for i in range(n+1):
        if i%2==1:
            answer.append(i)
    return answer