def solution(arr):
    answer = []
    if (len(arr)&(len(arr)-1))==0:
        answer=arr
        return answer
    else:
        while(len(arr)&(len(arr)-1)!=0):
            arr.append(0)
    answer=arr
    return answer