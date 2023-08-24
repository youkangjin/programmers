def solution(my_string, letter):
    answer = ''
    i=0
    while(i<len(my_string)):
        if my_string[i] in letter:
            i+=1
        else:
            answer+=my_string[i]
            i+=1
    return answer