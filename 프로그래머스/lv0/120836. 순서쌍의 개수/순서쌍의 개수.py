def solution(n):
    answer = 0
    i=1
    while(i<=len(range(n))):
        if n%i==0:
            answer+=1
        i+=1
    return answer