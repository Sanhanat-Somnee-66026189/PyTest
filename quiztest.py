def pingPong(bloodP,sugar) -> str :
    status = 'normal'
    stage = 'stage '

    if bloodP <= 120 and sugar < 100 :
        return status
    elif bloodP <= 139 and sugar <= 125 :
        status = 'risk group'
        return status 
    else :
        if bloodP <= 159 and sugar <= 154 :
            return stage + '1'
        elif bloodP <= 179 and sugar <= 182:
            return stage + '2'
        else :
            return stage + '3'
#hello world