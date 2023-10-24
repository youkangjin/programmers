def solution(s):
    answer = True
    a=0
    for i in range(len(s)):
        if a==0 and s[i]==")":
            return False
        elif s[i]=="(":
            a+=1
        elif s[i]==")":
            a-=1
    if a == 0:
        return True
    elif a != 0:
        return False