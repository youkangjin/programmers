def solution(rsp):
    a=str(rsp)
    i=0
    result = ""
    while(i<len(a)):
        if a[i] == "2":
            result=result+"0"
        elif a[i] == "0":
            result=result+"5"
        elif a[i] == "5":
            result= result+"2"
        i=i+1
    return result