def solution(numbers, k):
    answer = 0
    i=0
    a=[]
    answer1=0
    while(i<k):
        if len(numbers)%2==0:
            for j in range(0,len(numbers),2):
                if answer==k:
                    break
                answer+=1
                answer1=numbers[j]
            i+=1
        elif len(numbers)%2==1:
            if i==0:
                for t in range(2):
                    for j in numbers:
                        a.append(j)
            for v in range(0,len(a),2):
                if answer==k:
                    break
                answer+=1
                answer1=a[v]
            i+=1
    return answer1