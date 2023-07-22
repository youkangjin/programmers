def solution(n):
    sum=0
    i=1
    if n%2==1:
        for i in range(i,n+1):
            if i%2==1:
                sum=sum+i
            i=i+1
        return sum
    else:
        for i in range(i,n+1):
            if i%2==0:
                sum=sum+(i*i)
            i=i+1
        return sum