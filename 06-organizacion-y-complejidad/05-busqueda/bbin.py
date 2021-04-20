"""
Ejercicio 6.14: B√∫squeda binaria
Modificando la funci√≥n busqueda_binaria(lista, x) adecuadamente, defin√≠ una funci√≥n donde_insertar(lista, x) de forma que reciba una lista ordenada y un elemento y devuelva la posici√≥n de ese elemento en la lista (si se encuentra en la lista) o la posici√≥n donde se podr√≠a insertar el elemento para que la lista permanezca ordenada (si no est√° en la lista).

Por ejemplo: el elemento 3 podr√≠a insertarse en la posici√≥n 2 en la lista [0,2,4,6] para mantenerla ordenada. Por lo tanto, el llamado donde_insertar([0,2,4,6], 3) deber√° devolver 2, al igual que el llamado donde_insertar([0,2,4,6], 4).

Guarda tu modificaci√≥n en un archivo bbin.py.
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

lista = [1, 2, 5, 6, 7]
e = 100

donde_insertar(lista, e)

