def solution(hp):
    a=5
    b=3
    c=1
    d=0
    e=0
    f=0
    while(hp>0):
        if(a<=hp):
            hp=hp-5
            d=d+1
        elif(b<=hp):
            hp=hp-3
            e=e+1
        elif(c<=hp):
            hp=hp-1
            f=f+1
    return d+e+f