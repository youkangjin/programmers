def solution(numbers):
    answer = 0
    d=0
    a=[]
    b=[]
    i=0
    j=0
    for i in range(i, len(numbers)):
        if answer<numbers[i]:
            answer=numbers[i]
    a.append(answer)
    numbers.remove(answer)
    for j in range(j, len(numbers)):
        if d <numbers[j]:
            d=numbers[j]
    return d*answer