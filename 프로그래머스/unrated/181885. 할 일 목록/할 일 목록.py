def solution(todo_list, finished):
    answer = []
    a=""
    for i in range(0, len(todo_list)):
        a=str(finished[i]) 
        if a in "False":
            answer.append(todo_list[i])
    return answer