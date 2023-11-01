def solution(arr):
    answer = []
    answer1=arr
    a=range(len(arr))
    b=0
    if a==1:
        return 0
    for j in a:
        answer = []
        for i in answer1:
            if i > 50 and i%2==0:
                answer.append(i//2)
            elif i < 50 and i%2==1:
                answer.append(i*2+1)
            else:
                answer.append(i)
        b+=1
        if answer ==answer1:
            b-=1
            break
        answer1=answer
    return b