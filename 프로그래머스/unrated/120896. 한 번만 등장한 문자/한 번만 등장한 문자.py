def solution(s):
    answer = ''
    for i in s:
        a=0
        for j in s:
            if i==j:
                a+=1
        if a<=1:
            answer+=i
    b=''.join(sorted(answer))  
                
    return b