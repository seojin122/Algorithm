def solution(num_list):
    odd_num = sum(num_list[::2])
    even_num = sum(num_list[1::2])
    return odd_num if odd_num > even_num else even_num
     