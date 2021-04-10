"""
Ejercicio 4.6: Búsquedas de un elemento
Creá el archivo busqueda_en_listas.py para guardar tu código de este ejercicio y el siguiente.

En este primer ejercicio tenés que escribir una función buscar_u_elemento() que reciba una lista y un elemento y devuelva la posición de la última aparición de ese elemento en la lista (o -1 si el elemento no pertenece a la lista).

Probá tu función con algunos ejemplos:

>>> buscar_u_elemento([1,2,3,2,3,4],1)
0
>>> buscar_u_elemento([1,2,3,2,3,4],2)
3
>>> buscar_u_elemento([1,2,3,2,3,4],3)
4
>>> buscar_u_elemento([1,2,3,2,3,4],5)
-1

Agregale a tu programa busqueda_en_listas.py una función buscar_n_elemento() que reciba una lista y un elemento y devuelva la cantidad de veces que aparece el elemento en la lista. Probá también esta función con algunos ejemplos.
"""

def buscar_u_elemento(lista, elemento):
    posicion = -1 # en caso de no encontrarse el elemento
    contador = 0
    for x in lista:
        if x == elemento:
            posicion = contador
        contador += 1
    return posicion
    
test_1 = buscar_u_elemento([1,2,3,2,3,4],3)
test_2 = buscar_u_elemento([1,2,3,2,3,4],2)
test_3 = buscar_u_elemento([1,2,3,2,3,4],3)
test_4 = buscar_u_elemento([1,2,3,2,3,4],5)
print(test_1, test_2, test_3, test_4)

def buscar_n_elemento(lista, elemento):
    contador = 0 
    for x in lista: 
        if x == elemento:  
            contador += 1  
    return contador
    
cantidad = buscar_n_elemento([1, 1, 1, 1, 20], 20)
print(cantidad)
