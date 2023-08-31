def solution(my_string, is_suffix):
    answer1=0
    answer =""
    i=1
    while(i<len(my_string)+1):
        answer+=my_string[-i]
        if answer[::-1] == is_suffix:
            answer1=1
            break
        i+=1
    return answer1