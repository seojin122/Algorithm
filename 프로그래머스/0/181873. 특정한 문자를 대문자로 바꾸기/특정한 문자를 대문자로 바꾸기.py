def solution(my_string, alp):
    my_string = list(my_string)
    for num, word in enumerate(my_string):
        if word == alp:
            my_string[num] = my_string[num].upper()
    return "".join(my_string)