def solution(a, b):
    a_b = str(a)+str(b)
    if int(a_b) > (2*a*b):
        return int(a_b)
    else:
        return 2*a*b