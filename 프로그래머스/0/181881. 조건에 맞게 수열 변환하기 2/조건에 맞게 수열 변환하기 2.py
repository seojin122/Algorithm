def solution(arr):
    question=arr
    num=0
    while(True):
        answer=[]
        for i in question:
            if i >50 and i %2 == 0:
                answer.append(i//2)
            elif i<50 and i % 2 == 1:
                answer.append((i*2)+1)
            else:
                answer.append(i)
        if answer == question:
            return num
        question = answer
        num +=1