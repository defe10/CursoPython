def redondear(numero):
    num_ent = int(numero)
    num_dec = numero - num_ent
    
    if num_dec >= 0.5:
        return int(numero+1)
    else:
        return int(numero)