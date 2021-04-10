"""
Ejercicio 4.9: Propagación
Imaginate una fila con varios fósforos uno al lado del otro. Los fósforos pueden estar en tres estados: nuevos, prendidos fuego o ya gastados (carbonizados). Representaremos esta situación con una lista L con un elemento por fósforo, que en cada posición tiene un 0 (nuevo), un 1 (encendido) o un -1 (carbonizado). El fuego se propaga inmediatamente de un fósforo encendido a cualquier fósforo nuevo que tenga a su lado. Los fósforos carbonizados no se encienden nuevamente.

Escribí una función llamada propagar que reciba un vector con 0's, 1's y -1's y devuelva un vector en el que los 1's se propagaron a sus vecinos con 0. Guardalo en un archivo propaga.py.

Por ejemplo:

>>> propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0])
[ 0, 0, 0,-1, 1, 1, 1, 1,-1, 1, 1, 1, 1]
>>> propagar([ 0, 0, 0, 1, 0, 0])
[ 1, 1, 1, 1, 1, 1]
"""

# Adaptado de Javier Ceferino Rodriguez

def invertir_lista(lista):
    invertida = []
    i = 0 
    for x in lista:
        i -= 1
        invertida.append(lista[i])
    return invertida

def propagar(fosforos):
    n = len(fosforos) 
    prendido = 1
    apagado = -1
    nuevo = 0
    fosforos_der = [] # lista recorrida hacia la derecha
    fosforos_izq = [] # lista recorrida hacia la izquierda
    flag = 0 # referencia
    for i in range(0, n):
        fosforo = fosforos[i]
        if fosforo == prendido:
            flag = 1
        elif fosforo == apagado:
            flag = 0
        if (fosforo == nuevo) and (flag == 1):
            fosforos_der.append(1)
        else:
            fosforos_der.append(fosforo)
    for i in range(n-1, -1, -1): # para que vaya hacia atras de uno en uno
        fosforo = fosforos_der[i]
        if fosforo == prendido:
            flag = 1
        elif fosforo == apagado:
            flag = 0
        if (fosforo == nuevo) and (flag == 1):
            fosforos_izq.append(1)
        else:
            fosforos_izq.append(fosforo)
    fosforos_izq = invertir_lista(fosforos_izq)
    return fosforos_izq

test_1 = propagar([0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0])
test_2 = propagar([0, 0, 0, 1, 0, 0])
print(test_1, test_2)

