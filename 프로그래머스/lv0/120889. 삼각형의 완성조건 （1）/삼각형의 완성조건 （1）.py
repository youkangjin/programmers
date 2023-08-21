def solution(sides):
    answer = 0
    if sides[0]>=sides[1]+sides[2] and (sides[0]>sides[1] and  sides[0] >sides[2]):
        answer=2
    elif sides[1]>=sides[2]+sides[0] and (sides[1]>sides[0] and  sides[1] >sides[2]):
        answer=2
    elif sides[2]>=sides[1]+sides[0] and (sides[2]>sides[0] and  sides[2] >sides[1]):
        answer=2
    else:
        answer=1
            
    return answer