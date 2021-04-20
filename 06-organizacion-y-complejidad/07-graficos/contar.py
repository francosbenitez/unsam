"""
Ejercicio 6.19: Contar comparaciones en la b√∫squeda binaria
Modific√° el c√≥digo de b√∫squeda binaria (busqueda_binaria(lista, x)) introducido en la Secci√≥n 6.5, de forma que devuelva (adem√°s de la posici√≥n del elemento en la lista) la cantidad de comparaciones que realiz√≥ el algoritmo para encontrarlo o decidir que no est√°.
"""

def busqueda_lineal(lista, e):
    '''Si e est· en la lista devuelve su posiciÛn, de lo
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
    '''B˙squeda binaria
    PrecondiciÛn: la lista est· ordenada
    Devuelve -1 si x no est· en lista;
    Devuelve p tal que lista[p] == x, si x est· en lista
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 
    izq = 0
    der = len(lista) - 1
    n_comparaciones = 0
    while izq <= der:
        n_comparaciones += 1
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     
        if lista[medio] > x:
            der = medio - 1 
        else:               
            izq = medio + 1 
    return pos, n_comparaciones

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
    pos = busqueda_binaria(lista, x)[0]
    if pos == -1:
        pos = donde_insertar(lista, x)
        lista.insert(pos, x)
    return pos


def busqueda_secuencial(lista, x):
    '''Si x est· en la lista devuelve el Ìndice de su primera apariciÛn, 
    de lo contrario devuelve -1.
    '''
    pos = -1
    for i,z in enumerate(lista):
        if z == x:
            pos = i
            break
    return pos

def busqueda_secuencial_(lista, x):
    '''Si x est· en la lista devuelve el Ìndice de su primera apariciÛn, 
    de lo contrario devuelve -1. Adem·s devuelve la cantidad de comparaciones
    que hace la funciÛn.
    '''
    comps = 0 
    pos = -1
    for i,z in enumerate(lista):
        comps += 1 
        if z == x:
            pos = i
            break
    return pos, comps

mi_lista = [1, 2, 4, 5, 999, 1000]
valor = 100
insertar(mi_lista, valor)
