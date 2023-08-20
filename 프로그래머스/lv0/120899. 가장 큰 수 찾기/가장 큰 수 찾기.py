def solution(array):
    answer = []
    i=0
    a=0
    for i in range(len(array)):
        if i==0:
            a=array[0]
        elif a<array[i]:
            a=array[i]
        else:
            i=i+1
    answer.append(a)
    b=array.index(a)
    answer.append(b)
        
    return answer