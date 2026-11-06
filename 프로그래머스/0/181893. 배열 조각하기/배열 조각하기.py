def solution(arr, query):
    for inx, q in enumerate(query):
        if inx % 2 == 0: #짝수
            arr = arr[:q+1]
        else: #홀수
            arr = arr [q:]
    return arr