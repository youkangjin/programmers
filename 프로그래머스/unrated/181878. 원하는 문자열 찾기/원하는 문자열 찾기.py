def solution(myString, pat):
    answer = 0
    a=myString.lower()
    b=pat.lower()
    if b in a:
        answer=1
    else:
        answer=0
    return answer