import math

def solution(signals):
    
    #주기
    T = 1
    for g, y, r in signals:
        T = math.lcm(T, g+y+r)
    
    #노랑색 신호등
    
    for t in range(1, 1+T):
        yellow = True
        for g, y, r in signals:
            curr = (t) % (g+y+r)
            if not (g < curr <= g+y):
                yellow = False
                break
        
        if yellow :
            return t
    
    return -1