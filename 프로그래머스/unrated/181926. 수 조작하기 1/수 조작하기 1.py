def solution(n, control):
    i=0
    for i in range(i,len(control)):
        if control[i] in "w":
            n=n+1
        elif control[i] in "s":
            n=n-1
        elif control[i] in "d":
            n=n+10
        elif control[i] in "a":
            n=n-10
        i=i+1
    return n