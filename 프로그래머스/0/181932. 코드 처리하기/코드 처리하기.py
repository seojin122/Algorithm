def solution(code):
    ret=[]
    mode=False
    for i in range(len(code)):
        if code[i] == "1":
            mode = not mode
            continue
            
        if not mode and i%2==0:
            ret.append(code[i])
        elif mode and i%2==1:
            ret.append(code[i])

    answer = "".join(ret)
    return answer if answer else "EMPTY"