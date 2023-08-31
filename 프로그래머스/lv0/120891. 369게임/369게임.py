def solution(order):
    answer = 0
    a=list(str(order))
    for i in range(len(a)):
        if a[i] == "3" or a[i] == "6" or a[i] =="9":
            answer+=1
    return answer