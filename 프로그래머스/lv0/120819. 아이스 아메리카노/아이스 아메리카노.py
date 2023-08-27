def solution(money):
    answer = []
    a=0
    b=0
    a=int(money/5500)
    b=money%5500
    answer.append(a)
    answer.append(b)
    return answer