def solution(array, n):
    answer = 0
    i=0
    for i in range(i, len(array)):
        if array[i]==n:
            answer=answer+1
    return answer