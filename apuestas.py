def devolvertipo(elemento):
    return type(elemento)

def filtrar(lista, filtro):
    return filter(lambda x: type(x) == filtro, lista)

def verificariguales(lista, funcion):
    if len(filtrar(lista,bool)) == len(filtrar(lista,int)):
        if funcion == "pierde":
            return sumartodo(filtrar(lista,int)) - sumartodo(prueba(lista))
        else:
            if funcion == "gana":
                return sumartodo(prueba(lista))
    else:
        return ["no se puede ya que el numero de apuestas no es igual al numero de si gano o no"]
def sumartodo(lista):
    return reduce(lambda x,y: x+y,lista)
def prueba(lista):
    return map(lambda x,y: x if y ==True else 0 , filtrar(lista,int), filtrar(lista, bool))
def cuantoperdio(matriz):
    return map(lambda x: verificariguales(x,"pierde"), matriz)
def cuantogano(matriz):
    return map(lambda x : verificariguales(x,"gana"), matriz)
def entrada(matriz):
    return  "el jugador que mas perdio fue el jugador numero "+str(sacarindex(cuantoperdio(matriz),quien(cuantoperdio(matriz)))+1)+" y perdio " + str(quien(cuantoperdio(matriz)))+ " y el que mas gano fue el jugador "+str(sacarindex(cuantogano(matriz),quien(cuantogano(matriz)))+1)+" y gano "+str(quien(cuantogano(matriz)))

def quien(lista):
    return reduce(lambda x,y: x if (x > y) else y, lista)

def sacarindex(lista,numero):
    return lista.index(numero)




