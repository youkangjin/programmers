def solution(s):
    num=['zero','one','two','three','four','five','six','seven','eight','nine']
    for a,b in enumerate(num):
        s=str(a).join(s.split(b))
        
    
    return int(s)