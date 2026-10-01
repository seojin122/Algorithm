def solution(n):
    sum = 0
    if n % 2 == 0 :# 짝수
        i=0
        for _ in range(n//2):
            print(sum)
            i += 2
            sum += i**2
            

    else:
        i = 1
        for _ in range((n//2)+1):
            print(sum)
            sum += i
            i += 2
            
            
    return sum