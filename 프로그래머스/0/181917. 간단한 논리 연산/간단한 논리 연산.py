def solution(x1, x2, x3, x4):
    answer1 = True
    answer2 = True
    answer3 = True
    
    if x1 or x2:
        answer1 = True
    else:
        answer1 = False
        
    if x3 or x4:
        answer2 = True
    else:
        answer2 = False
        
        
    if answer1 and answer2:
        answer3 = True
    else:
        answer3 = False
        
    return answer3