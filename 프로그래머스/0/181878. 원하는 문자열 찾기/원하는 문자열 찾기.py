def solution(myString, pat):
    myString = myString.lower()
    pat = pat.lower()
    print(myString)
    print(pat)
    if pat in myString:
        return 1
    else:
        return 0