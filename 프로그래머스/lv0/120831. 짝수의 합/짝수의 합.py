def solution(n):
    answer = 0
    i=1
    for i in range(n+1):
        if i%2==0:
            answer=answer+i
    return answer