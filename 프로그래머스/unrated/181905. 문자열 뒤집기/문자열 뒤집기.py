def solution(my_string, s, e):
    answer = ''
    answer += my_string[:s]
    b=my_string[s:e+1]
    answer += b[::-1]
    answer += my_string[e+1:]
    return answer