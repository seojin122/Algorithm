def solution(arr):
    double=[]
    answer=[]
    for i in range(len(arr)):
        if arr[i] == 2:
            double.append(i)
    if double:
        return arr[double[0]:double[-1]+1]
    else:
        return [-1]