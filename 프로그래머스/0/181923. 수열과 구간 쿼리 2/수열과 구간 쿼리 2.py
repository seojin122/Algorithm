def solution(arr, queries):
    answer=[]
    for s, e, k in queries:
        litter=[]
        for j in arr[s:e+1]:
            if k<j:
                litter.append(j)       
        if litter:
            litter.sort()    
            answer.append(litter[0])
        else: 
            answer.append(-1)
        
    return answer