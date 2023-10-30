def solution(my_string):
    answer = 0
    st=""
    for i in my_string:
        if i.isdigit():
            st+=i
        else:
            if len(st)==0:
                continue
            answer+=int(st)
            st=""
    if len(st) != 0:
        answer+=int(st)
    return answer