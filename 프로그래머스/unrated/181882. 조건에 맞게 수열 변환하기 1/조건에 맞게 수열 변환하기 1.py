def solution(arr):
    answer = []
    i=0
    for i in range(0, len(arr)):
        if arr[i]<50 and arr[i]%2==1:
            answer.append(arr[i]*2)
        elif arr[i]>=50 and arr[i]%2==0:
            answer.append(arr[i]/2)
        else:
            answer.append(arr[i])
    return answer