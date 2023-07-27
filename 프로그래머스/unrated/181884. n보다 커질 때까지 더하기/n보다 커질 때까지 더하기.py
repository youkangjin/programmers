def solution(numbers, n):
    i=0
    x=0
    for i in range(i,len(numbers)):
        x=numbers.pop(0)+x
        if x>n:
            return x
        elif x<n:
            i=i+1