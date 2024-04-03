def solution(n):
    answer = []
    i = 2
    while i <= n:
        if n % i == 0:
            n = n // i
            if len(answer) == 0 or answer[-1] != i:
                answer.append(i)
        else:
            i += 1
    return answer
