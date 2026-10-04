def solution(a, d, included):
    sum = 0
    for i in range(len(included)):
        answer = d*i + a
        if included[i]:
            sum += answer
    return sum