"""
Ejercicio 6.15: Insertar un elemento en una lista
Uno de los problemas de la búsqueda binaria es que requiere que la lista esté ordenada. Si la lista se encuentra ordenada podemos mantener el orden evitando adjuntar nuevos elementos de forma desordenada.

Usando lo que hiciste en el Ejercicio 6.14, agregale al archivo bbin.py una función insertar(lista, x) que reciba una lista ordenada y un elemento. Si el elemento se encuentra en la lista solamente devuelve su posición; si no se encuentra en la lista, lo inserta en la posición correcta para mantener el orden. En este segundo caso, también debe devolver su posición.
"""

def busqueda_lineal(lista, e):
    '''Si e está en la lista devuelve su posición, de lo
    contrario devuelve -1.
    '''
    pos = -1  
    for i, z in enumerate(lista): 
        if z == e:   
            pos = i  
            break    
    return pos

def busqueda_lineal_lordenada(lista,e):
    sorted_list = sorted(lista)
    pos = -1  
    for i, z in enumerate(sorted_list): 
        if z == e:   
            pos = i  
            break    
    return pos

def busqueda_binaria(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     
        if lista[medio] > x:
            der = medio - 1 
        else:               
            izq = medio + 1 
    return pos

def donde_insertar(lista, x):
    pos = -1 
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if lista[medio] == x:
            pos = medio     
        if lista[medio] > x:
            der = medio - 1 
            var = True
        else:               
            izq = medio + 1 
            var = False
    if pos == -1:
        pos = medio if var == True else medio + 1
    return pos

def insertar(lista, x):
    pos = busqueda_binaria(lista, x)
    if pos == -1:
        pos = donde_insertar(lista, x)
        lista.insert(pos, x)
    return pos

mi_lista = [1, 2, 4, 5, 999, 1000]
valor = 100
insertar(mi_lista, valor)