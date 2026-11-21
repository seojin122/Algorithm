def solution(strArr):
    for i, val in enumerate(strArr):
        if i % 2 == 0:
            strArr[i] = val.lower()
        else:
            strArr[i] = val.upper()
    return strArr