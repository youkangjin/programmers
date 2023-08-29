def solution(code):
    answer = ''
    a=0
    for i in range(len(code)):
        if code[i]=="1":
            if a==0:
                a=1
            elif a==1:
                a=0
        elif a==0:
            if i%2==0:
                answer+=code[i]
        elif a==1:
            if i%2==1:
                answer+=code[i]
    if answer == '':
        answer = "EMPTY"
    return answer