def solution(my_string):
    a=my_string.split()
    b=0
    for i in range(len(a)):
        if i==0:
            b=int(a[0])
        elif a[i] == "+":
            b+=int(a[i+1])
        elif a[i] == "-":
            b-=int(a[i+1])
    
    return b