def solution(id_list, report, k):
    answer = []
    iduser_idreport={}
    stop_user=[]
    person_user=[]
    id_sum=[0]*len(id_list)
    for i in report:
        id_user,id_report=i.split()
        if id_report in iduser_idreport:
            iduser_idreport[id_report].append(id_user)
        else:
            iduser_idreport[id_report]=[id_user]
    
    for key,value in iduser_idreport.items():
        iduser_idreport[key]=list(set(value))
        if len(iduser_idreport[key]) >=k:
            stop_user.append(key)
            person_user.append(iduser_idreport[key])
    
    for i in range(len(person_user)):
        for j in range(len(person_user[i])):
            id_sum[id_list.index(person_user[i][j])]+=1
    return id_sum