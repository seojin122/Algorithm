def solution(num_list):
    for i in range(len(num_list)):
        if num_list[i] < 0:
            return i
    return -1
# return next((i for i, x in enumerate(num_list) id x<0), -1)