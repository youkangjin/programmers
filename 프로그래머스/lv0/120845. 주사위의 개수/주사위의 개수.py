def solution(box, n):
    answer = 0
    i=0
    a=1
    for i in range(i, len(box)):
        a=int(box[i]/n)*a
    answer=a
    return answer