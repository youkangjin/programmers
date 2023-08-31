def solution(my_string, is_prefix):
    answer = 0
    answer1 = ""
    for i in range(len(my_string)):
        answer1 += my_string[i]
        if answer1 == is_prefix:
            answer = 1
            break
    return answer