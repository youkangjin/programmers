def solution(a, b):
    x=str(a)+str(b)
    x=int(x)
    y=2*int(a)*int(b)
    if x>=y:
        return x
    else:
        return y