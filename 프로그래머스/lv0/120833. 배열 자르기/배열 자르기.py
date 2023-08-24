def solution(numbers, num1, num2):
    answer = []
    while(num1<=num2):
        answer.append(numbers[num1])
        num1+=1
    return answer