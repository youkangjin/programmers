def solution(arr, k):
    answer = []
    i=0
    if k%2==1:
        while(i<len(arr)):
            answer.append(arr[i]*k)
            i+=1
    else:
        while(i<len(arr)):
            answer.append(arr[i]+k)
            i+=1
    return answer