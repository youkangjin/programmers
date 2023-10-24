def solution(picture, k):
    answer = []
    a=""
    for i in picture:
        a=""
        for j in i:
            for d in range(k):
                a+=j
        for c in range(k):
            answer.append(a)
        
    
    return answer