def solution(todo_list, finished):
    answer=[]
    for num, is_it in enumerate(finished):
        if not is_it:
            answer.append(todo_list[num])
    return answer
