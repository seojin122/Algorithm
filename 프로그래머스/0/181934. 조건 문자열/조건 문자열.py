def solution(ineq, eq, n, m):
    if eq == "=" and ineq == "<" and n<=m:
        return 1
    elif eq == "=" and ineq == ">" and n>=m:
        return 1
    elif eq == "!" and ineq == "<" and n<m:
        return 1
    elif eq == "!" and ineq == ">" and n>m:
        return 1
    else:
        return 0