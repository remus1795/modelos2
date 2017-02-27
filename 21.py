import random

def hacerpinta(pinta, numero):
    if numero <= 10:
        return [[numero, pinta]]+hacerpinta(pinta, numero+1)
    else:
        if numero > 10:
            if numero == 11:
                return [["J", pinta]]+hacerpinta(pinta, numero+1)
            else:
                if numero == 12:
                     return [["Q", pinta]]+hacerpinta(pinta, numero+1)
                else:
                    if numero ==13:
                         return [["K", pinta]]+hacerpinta(pinta, numero+1)
                    else:
                        if numero >= 14:
                            return []

def hacernaipecompleto():
    return hacerpinta("diamante",1)+hacerpinta("corazones",1)+hacerpinta("picas",1)+hacerpinta("trebol",1)

def sacarcarta(lista):
    return [lista.pop(random.randrange(1,53))]+[lista.pop(random.randrange(1,53))]
def prueba(lista):
    return [lista.pop(random.randrange(1,53))]+[lista]
def barajar(lista):
    random.shuffle(lista)
    return lista
def sacarprimeracarta(lista):
    return [lista.pop(0)]
def actualizarbaraja(lista):
    return lista[1:]
    
def proceso():
    return sacarprimeracarta(barajar(hacernaipecompleto()))








    
                        
                    
                    
               
            
        
