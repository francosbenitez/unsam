"""
Ejercicio 4.8: Invertir una lista
Escribí una función invertir_lista(lista) que dada una lista devuelva otra que tenga los mismos elementos pero en el orden inverso. Es decir, el que era el primer elemento de la lista de entrada deberá ser el último de la lista de salida y análogamente con los demás elementos.

def invertir_lista(lista):
    invertida = []
    for e in lista: # Recorro la lista
        ... #agrego el elemento e al principio de la lista invertida
    return invertida
Guardá la función en el archivo invlista.py y probala con las siguientes listas:

[1, 2, 3, 4, 5]
['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']
"""

def invertir_lista(lista):
    invertida = []
    i = 0 # agrego contador para atrás
    for x in lista:
        i -= 1
        invertida.append(lista[i])
    return invertida

test_1 = invertir_lista([1, 2, 3, 4, 5])
print(test_1)

test_2 = invertir_lista(['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel'])
print(test_2)