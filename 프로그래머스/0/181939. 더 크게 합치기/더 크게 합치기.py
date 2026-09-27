def solution(a, b):
    a_b = str(a) + str(b)
    b_a = str(b) + str(a)
    if int(a_b) > int(b_a):
        return int(a_b)
    else:
        return int(b_a)