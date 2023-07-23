def solution(ineq, eq, n, m):
    if ineq in ">":
        if eq in "=":
            if n>=m:
                return 1
            else:
                return 0
        elif eq in "!":
            if n>m:
                return 1
            else:
                return 0
    if ineq in "<":
         if eq in "=":
            if n<=m:
                return 1
            else:
                return 0
         elif eq in "!":
             if n<m:
                return 1
             else:
                return 0