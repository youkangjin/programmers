def solution(rny_string):
    i=0
    a=rny_string.count("m")
    if a==0:
        return rny_string
    else:
        for i in range(i, a):
            b=rny_string.replace("m", "rn")
            i=i+1
        return b
            