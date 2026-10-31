def solution(n, k):
    answer = []
    j = k
    while(j <= n):
        answer.append(j)
        j += k
    return answer