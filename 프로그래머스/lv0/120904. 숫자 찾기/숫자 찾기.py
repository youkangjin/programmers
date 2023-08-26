def solution(num, k):
    answer = 0
    a=""
    b=""
    a=str(num)
    b=str(k)
    for i in range(len(a)):
        if a[i] in b:
            answer=i+1
            break
        elif answer == 0:
                answer=-1
        
    return answer