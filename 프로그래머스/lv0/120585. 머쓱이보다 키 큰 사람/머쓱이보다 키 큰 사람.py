def solution(array, height):
    answer = 0
    i=0
    for i in range(i, len(array)):
        if array[i]>height:
            answer=answer+1
    return answer