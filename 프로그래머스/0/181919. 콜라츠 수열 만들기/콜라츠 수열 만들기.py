def solution(n):
    answer = [n]
    while (n!=1):
        if n % 2 == 1:#홀수
            n = 3*n + 1
        else:
            n = n // 2
            print(n)
        answer.append(n)
    return answer 