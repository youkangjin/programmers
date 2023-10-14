def solution(arr, flag):
    answer = []
    for i ,j in zip(arr, flag):
        if j==True:
            for z in range(i*2):
                answer.append(i)
        else:
            for s in range(i):
                del answer[-1]
                
    return answer