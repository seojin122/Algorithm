def solution(num_list):
    num=0
    for i in num_list:
        while(i!=1):
            i//=2
            num += 1
    return num