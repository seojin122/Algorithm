def solution(str_list):
    for i, num in enumerate(str_list):
        if num == "l":
            return str_list[:i]
        elif num =="r":
            return str_list[i+1:]
    return []