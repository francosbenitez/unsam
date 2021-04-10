"""
Ejercicio 4.1: Debugger
Ingresá y corré el siguiente código en tu IDE:

def invertir_lista(lista):
    '''Recibe una lista L y la develve invertida.'''
    invertida = []
    i=len(lista)
    while i > 0:    # tomo el último elemento 
        i=i-1
        invertida.append (lista.pop(i))  #
    return invertida

l = [1, 2, 3, 4, 5]    
m = invertir_lista(l)
print(f'Entrada {l}, Salida: {m}')
Deberías observar que la función modifica el valor de la lista de entrada. Eso no debería ocurrir: una función nunca debería modificar los parámetros salvo que sea lo esperado. Usá el debugger y el explorador de variables para determinar cuál es el primer paso clave en el que se modifica el valor de esta variable.
"""

def invertir_lista(lista):
    '''Recibe una lista L y la develve invertida.'''
    invertida = []
    i=len(lista)
    while i > 0:    # tomo el último elemento 
        i=i-1
        invertida.append(lista[i])  # la función pop quita 
    return invertida

l = [1, 2, 3, 4, 5]    
m = invertir_lista(l)
print(f'Entrada {l}, Salida: {m}')