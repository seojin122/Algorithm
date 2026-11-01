def solution(my_string, indices):
    indices_set = set(indices)
    answer = []
    for i, ch in enumerate(my_string):
        if i not in indices_set:
            answer.append(ch)
        
    return ''.join(answer)