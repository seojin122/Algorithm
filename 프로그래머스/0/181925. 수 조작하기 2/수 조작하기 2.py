def solution(numLog):
    control=[]
    for i in range(len(numLog)-1):
        diff = numLog[i + 1] - numLog[i]
        match diff:
            case 1: control.append("w")
            case -1: control.append("s")
            case 10: control.append("d")
            case -10: control.append("a")
               
    return "".join(control)