a=[10,80,15,30,20]
b=[20,45,80,20,10]
c=[20,35,60,90,20]

intercect= list []
def valores_comunes():
    for d in a:
        for e in b:
            for f in c:
                if e == d and e ==f:
                    intercect.append (e)
                    return set (intercect)

lista_completa=[]:
def conc():
    lista_completa =a+b+c
    return lista_completa
def eliminar_duplicado():
    lista_completa= set (lista_completa)
    return lista_completa
def descendente():
    lista_completa=list (lista_completa)
    lista_completa= lista_completa.sort()
    lista_completa= lista_completa[::-1]
    return lista_completa