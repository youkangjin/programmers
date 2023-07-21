def solution(a, b):
    answer = str(a)+str(b)
    answer = int(answer)
    answer1 = str(b)+str(a)
    answer1 = int(answer1)
    if answer>=answer1:
        return answer
    else:
        return answer1