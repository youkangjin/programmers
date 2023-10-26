def solution(arr):
    answer = []
    for i, j in enumerate(arr):
        if j==2:
            answer.append(i)
    if len(answer)==1:
        return [2]
    elif len(answer)==0:
        return [-1]
            
    return arr[answer[0]:answer[-1]+1]