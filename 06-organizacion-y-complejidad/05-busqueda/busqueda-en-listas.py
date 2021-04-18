"""
Ejercicio 6.13: Búsqueda lineal sobre listas ordenadas.
Modificá la función busqueda_lineal(lista, e) de la Sección 4.2 para el caso de listas ordenadas, de forma que la función pare cuando encuentre un elemento mayor a e. Llamá a tu nueva función busqueda_lineal_lordenada(lista,e) y guardala en el archivo busqueda_en_listas.py.

En el peor caso, ¿cuál es nuestra nueva hipótesis sobre comportamiento del algoritmo? ¿Es realmente más eficiente?
"""

def busqueda_lineal(lista, e):
    '''
    Si hay un elemento mayor a e, la funcion para.
    '''
    pos = -1  
    for i, z in enumerate(lista): 
        if z > e:   
            pos = i  
            break    
    return pos

print(busqueda_lineal([1, 4, 54, 3, 0, -1], 44),
busqueda_lineal([1, 4, 54, 3, 0, -1], 3),
busqueda_lineal([1, 4, 54, 3, 0, -1], 0),
busqueda_lineal([], 42))