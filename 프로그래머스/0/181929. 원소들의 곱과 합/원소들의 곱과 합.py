def solution(num_list):
    multiply_sum = 1
    square_sum = 0
    for i in range(len(num_list)):
        multiply_sum *= num_list[i]
        square_sum += num_list[i]
    if multiply_sum <= (square_sum**2):
        return 1
    else:
        return 0